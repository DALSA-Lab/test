# Source Directory

This project repository organizes **all code as packages**—both Python and C++ inside `src`.  
Each package is self‑contained and can be built and linted independently.

---

## Package Layout

### Python packages
- Must contain an `__init__.py`
- Documented with **NumPy-style** docstrings

```
py_pkg
├─ math_utils.py
├─ module.py
├─ README.md
├─ string_utils.py
└─ __init__.py

```

### C++ packages
- Typical structure is **include/** (public headers) + **src/** (implementation)
- Built with **CMake** (each C++ package has its own `CMakeLists.txt`)
- Documented with **Doxygen-style** comments and surfaced in Sphinx via **Breathe**

```
cpp_pkg
├─ CMakeLists.txt
├─ include
│  ├─ math_utils.hpp
│  └─ string_utils.hpp
├─ README.md
├─ src
│  ├─ math_utils.cpp
│  └─ string_utils.cpp
└─ tests
   └─ test_main.cpp
```

> In short: **Python = modules with `__init__.py`**, **C++ = CMake subprojects with `include/` & `src/`**.

---

## Documentation

We autoamtically generate a single documentation site using **Sphinx**.  
- **Python:** Sphinx + `sphinx.ext.autodoc` (and `sphinx.ext.napoleon` for NumPy-style) pull docstrings directly.
- **C++:** `doxygen` parses the header/source comments; **Breathe** bridges Doxygen XML into Sphinx.

### Python docstrings (NumPy style)

```python
def square(x):
    """
    Calculate the square of a number.

    Parameters
    ----------
    x : float or int
        The number to be squared.

    Returns
    -------
    float or int
        The square of the input number.
    """
    return x * x
```

### C++ comments (Doxygen style)

> The block below is a **Doxygen** comment (also called a “Javadoc-style” or “Qt-style” comment).  
> Doxygen parses `/** ... */` plus tags like `@brief`, `@param`, `@return`.

```cpp
/**
 * @brief Calculate the square of a number.
 * @param x The number to be squared.
 * @return The square of the input number.
 */
double square(double x);
```

---

## Linting & Formatting (GitHub Actions)

We enforce code quality via CI:

- **Python:** `ruff` (linter + basic formatting), configured via `pyproject.toml` or `ruff.toml`
- **C++:** `clang-tidy` (static analysis) and `clang-format` (formatting), configured via `.clang-tidy` and `.clang-format`

### Local usage

```bash
# Python
ruff check src/my_python_pkg
ruff format src/my_python_pkg

# C++
clang-format -i $(git ls-files "src/cpp_pkg/**/*.[ch]pp" "src/cpp_pkg/**/*.[ch]")
clang-tidy -p src/cpp_pkg/build src/cpp_pkg/src/*.cpp -- -std=c++17
```

> Tip: keep a `.clang-format`, `.clang-tidy`, and `pyproject.toml` at the repo root so both local and CI runs stay consistent.

---

## ⚙️ CI Limitation (current state)

In our GitHub Actions, **you must manually list which packages to lint/build**.  
At the moment, the workflow does not auto-discover all Python/C++ packages. When you add a new package, you **must update the workflow YAML** to include it.

### Example matrix (simplified)

```yaml
# .github/workflows/ci.yml (snippet)
jobs:
  lint-python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        package:
          - src/my_python_pkg
          - src/another_python_pkg   # ← add new Python packages here
    steps:
      - uses: actions/checkout@v4
      - run: pip install ruff
      - run: ruff check ${{ matrix.package }}

  lint-cpp:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        pkg:
          - src/cpp_pkg               # ← add new C++ packages here
    steps:
      - uses: actions/checkout@v4
      - run: sudo apt-get update && sudo apt-get install -y cmake ninja-build clang-tidy clang-format
      - name: Configure (CMake)
        run: |
          cmake -S ${{ matrix.pkg }} -B ${{ matrix.pkg }}/build -G Ninja \
                -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
      - name: clang-format (check)
        run: |
          git ls-files "${{ matrix.pkg }}/**/*.hpp" "${{ matrix.pkg }}/**/*.cpp" | xargs -r clang-format --dry-run --Werror
      - name: clang-tidy
        run: |
          if command -v run-clang-tidy >/dev/null 2>&1; then
            run-clang-tidy -p ${{ matrix.pkg }}/build -j"$(nproc)" -- -std=c++17
          else
            for f in $(git ls-files "${{ matrix.pkg }}/src/*.cpp"); do
              clang-tidy -p "${{ matrix.pkg }}/build" "$f" -- -std=c++17
            done
          fi
```

---

## Adding a New Package — Checklist

1. **Create the package folder**
   - Python: `src/<new_python_pkg>/...` with `__init__.py`
   - C++: `src/<new_cpp_pkg>/include`, `src/<new_cpp_pkg>/src`, and a `CMakeLists.txt`
2. **Document**
   - Python: NumPy docstrings in all public functions/classes
   - C++: Doxygen comments in headers/sources
3. **Wire docs**
   - Add to `Doxyfile` / `breathe_projects` as needed
   - Ensure Sphinx can import Python package (e.g., `sys.path.insert(...)` in `conf.py` or use `-m sphinx`)
4. **Configure lint**
   - Ensure `ruff`, `.clang-tidy`, and `.clang-format` cover the new paths
5. **Update CI**
   - Add the new package path to the GitHub Actions matrix (Python/C++ jobs)

---

## Quick Glossary

- **NumPy-style docstring**: A widely used, structured format for Python docstrings that Sphinx (via `sphinx.ext.napoleon`) can parse automatically.
- **Doxygen**: A documentation generator for C/C++ that reads `/** ... */` comments and produces XML/HTML.
- **Breathe**: A Sphinx extension that reads Doxygen XML and exposes it to Sphinx directives, letting C++ API docs live in the same site as Python docs.
- **Ruff**: Fast Python linter/formatter.
- **clang-tidy / clang-format**: Static analysis and formatting tools for C/C++ based on LLVM/Clang.

---

## Conventions

- **Python** ≥ 3.10 (adjust if your project differs)
- **C++** standard: C++17 by default (`-std=c++17`) unless the package states otherwise
- Keep public APIs documented; treat warnings from linters as actionable

---

If you’re unsure about the correct place to put new code or docs, **open a short PR or issue** and we’ll help place it in the right package and wire up the CI.
