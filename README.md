# Auto Calib

> Short description of the project

## Project Structure
```
.
├── src/           # Source code (any language)
├── tests/         # Unit/integration tests
├── docs/          # Documentation (architecture, API, examples)
│   ├── architecture/
│   ├── api/
│   └── examples/
├── .github/       # Workflows (optional)
├── LICENSE
├── README.md
└── CHANGELOG.md
```

## Architecture & Design
- Start with `docs/architecture/overview.md`.
- Add/update the **system diagram** in `docs/architecture/system_diagram.md`.
- Add **component diagrams** in `docs/architecture/component_diagrams/`.

## How to Use
- See examples in `docs/examples/`.
- Provide minimal setup & run instructions here.

## API / Interfaces
- Document in `docs/api/`.
- If you expose HTTP endpoints, define them in `docs/api/openapi.yaml`.

## How to Contribute
See `CONTRIBUTING.md` for branching, coding style, PRs, and reviews.

## License
This project is licensed under the terms in `LICENSE`.

```
test
├─ .DS_Store
├─ .editorconfig
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ docs
│  ├─ .DS_Store
│  ├─ api
│  │  ├─ .DS_Store
│  │  ├─ cpp_pkg
│  │  │  ├─ classcpppkg_1_1_calculator.md
│  │  │  ├─ class_contents.md
│  │  │  ├─ class_index.md
│  │  │  ├─ compound-list.js
│  │  │  ├─ dir_0c963d1cbf18cb8e49a41793502d34d3.md
│  │  │  ├─ dir_68267d1309a1af8e8297ef4c3efbcdba.md
│  │  │  ├─ dir_ae5f9e36d6c970e85959cc61ed45e10e.md
│  │  │  ├─ dir_af0444ea0c7ec8635d6db1da8eb19d03.md
│  │  │  ├─ dir_contents.md
│  │  │  ├─ dir_index.md
│  │  │  ├─ file_contents.md
│  │  │  ├─ file_index.md
│  │  │  ├─ global_contents.md
│  │  │  ├─ global_index.md
│  │  │  ├─ index.md
│  │  │  ├─ namespacecpppkg.md
│  │  │  ├─ namespace_contents.md
│  │  │  ├─ namespace_index.md
│  │  │  ├─ README.md
│  │  │  ├─ sample_8cpp.md
│  │  │  └─ sample_8h.md
│  │  ├─ cpp_pkg.md
│  │  └─ module.md
│  ├─ architecture
│  │  ├─ .DS_Store
│  │  └─ component_diagrams
│  │     └─ component-template.md
│  ├─ doxygen
│  │  ├─ .DS_Store
│  │  ├─ html
│  │  │  ├─ annotated.html
│  │  │  ├─ annotated_dup.js
│  │  │  ├─ classcpppkg_1_1_calculator-members.html
│  │  │  ├─ classcpppkg_1_1_calculator.html
│  │  │  ├─ classcpppkg_1_1_calculator.js
│  │  │  ├─ classes.html
│  │  │  ├─ classmath__utils_1_1_calculator-members.html
│  │  │  ├─ classmath__utils_1_1_calculator.html
│  │  │  ├─ classmath__utils_1_1_calculator.js
│  │  │  ├─ classstring__utils_1_1_formatter-members.html
│  │  │  ├─ classstring__utils_1_1_formatter.html
│  │  │  ├─ classstring__utils_1_1_formatter.js
│  │  │  ├─ clipboard.js
│  │  │  ├─ cookie.js
│  │  │  ├─ dir_0c963d1cbf18cb8e49a41793502d34d3.html
│  │  │  ├─ dir_0c963d1cbf18cb8e49a41793502d34d3.js
│  │  │  ├─ dir_68267d1309a1af8e8297ef4c3efbcdba.html
│  │  │  ├─ dir_68267d1309a1af8e8297ef4c3efbcdba.js
│  │  │  ├─ dir_6f8b1b6f986a303525dc35d8218f7003.html
│  │  │  ├─ dir_6f8b1b6f986a303525dc35d8218f7003.js
│  │  │  ├─ dir_ae5f9e36d6c970e85959cc61ed45e10e.html
│  │  │  ├─ dir_af0444ea0c7ec8635d6db1da8eb19d03.html
│  │  │  ├─ dir_af0444ea0c7ec8635d6db1da8eb19d03.js
│  │  │  ├─ dir_c69c8bd29bd3a83e36667cbdf9edaa3b.html
│  │  │  ├─ dir_c69c8bd29bd3a83e36667cbdf9edaa3b.js
│  │  │  ├─ dir_dc130d65b69c161f9c96cbc86a44ccd1.html
│  │  │  ├─ doxygen.css
│  │  │  ├─ doxygen.svg
│  │  │  ├─ doxygen_crawl.html
│  │  │  ├─ dynsections.js
│  │  │  ├─ files.html
│  │  │  ├─ files_dup.js
│  │  │  ├─ functions.html
│  │  │  ├─ functions_func.html
│  │  │  ├─ index.html
│  │  │  ├─ jquery.js
│  │  │  ├─ math__utils_8hpp.html
│  │  │  ├─ math__utils_8hpp.js
│  │  │  ├─ math__utils_8hpp_source.html
│  │  │  ├─ menu.js
│  │  │  ├─ menudata.js
│  │  │  ├─ navtree.css
│  │  │  ├─ navtree.js
│  │  │  ├─ navtreedata.js
│  │  │  ├─ navtreeindex0.js
│  │  │  ├─ sample_8h_source.html
│  │  │  ├─ search
│  │  │  │  ├─ all_0.js
│  │  │  │  ├─ all_1.js
│  │  │  │  ├─ all_2.js
│  │  │  │  ├─ all_3.js
│  │  │  │  ├─ all_4.js
│  │  │  │  ├─ all_5.js
│  │  │  │  ├─ all_6.js
│  │  │  │  ├─ classes_0.js
│  │  │  │  ├─ classes_1.js
│  │  │  │  ├─ files_0.js
│  │  │  │  ├─ files_1.js
│  │  │  │  ├─ functions_0.js
│  │  │  │  ├─ functions_1.js
│  │  │  │  ├─ functions_2.js
│  │  │  │  ├─ functions_3.js
│  │  │  │  ├─ search.css
│  │  │  │  ├─ search.js
│  │  │  │  ├─ searchdata.js
│  │  │  │  ├─ variables_0.js
│  │  │  │  └─ variables_1.js
│  │  │  ├─ string__utils_8hpp.html
│  │  │  ├─ string__utils_8hpp.js
│  │  │  ├─ string__utils_8hpp_source.html
│  │  │  └─ tabs.css
│  │  └─ xml
│  │     ├─ classcpppkg_1_1_calculator.xml
│  │     ├─ classmath__utils_1_1_calculator.xml
│  │     ├─ classstring__utils_1_1_formatter.xml
│  │     ├─ combine.xslt
│  │     ├─ compound.xsd
│  │     ├─ dir_0c963d1cbf18cb8e49a41793502d34d3.xml
│  │     ├─ dir_68267d1309a1af8e8297ef4c3efbcdba.xml
│  │     ├─ dir_6f8b1b6f986a303525dc35d8218f7003.xml
│  │     ├─ dir_ae5f9e36d6c970e85959cc61ed45e10e.xml
│  │     ├─ dir_af0444ea0c7ec8635d6db1da8eb19d03.xml
│  │     ├─ dir_c69c8bd29bd3a83e36667cbdf9edaa3b.xml
│  │     ├─ dir_dc130d65b69c161f9c96cbc86a44ccd1.xml
│  │     ├─ Doxyfile.xml
│  │     ├─ doxyfile.xsd
│  │     ├─ index.xml
│  │     ├─ index.xsd
│  │     ├─ math__utils_8cpp.xml
│  │     ├─ math__utils_8hpp.xml
│  │     ├─ namespacecpppkg.xml
│  │     ├─ namespacemath__utils.xml
│  │     ├─ namespacestring__utils.xml
│  │     ├─ sample_8cpp.xml
│  │     ├─ sample_8h.xml
│  │     ├─ string__utils_8cpp.xml
│  │     ├─ string__utils_8hpp.xml
│  │     └─ xml.xsd
│  ├─ examples
│  │  └─ README.md
│  ├─ make.bat
│  ├─ Makefile
│  └─ source
│     ├─ architecture
│     │  ├─ component_diagrams
│     │  │  ├─ component-template.md
│     │  │  └─ index.rst
│     │  ├─ index.rst
│     │  └─ overview.md
│     ├─ conf.py
│     ├─ documentation
│     │  ├─ cpp_pkgs
│     │  │  ├─ cpp_pkg.rst
│     │  │  └─ index.rst
│     │  ├─ index.rst
│     │  └─ py_pkgs
│     │     ├─ index.rst
│     │     └─ py_pkg.rst
│     ├─ index.rst
│     └─ usage
│        └─ examples
│           ├─ example_1.md
│           ├─ example_2.md
│           └─ index.rst
├─ Doxyfile
├─ LICENSE
├─ mkdocs.yml
├─ README.md
├─ requirements-docs.txt
├─ src
│  ├─ .DS_Store
│  ├─ cpp_pkg
│  │  ├─ CMakeLists.txt
│  │  ├─ include
│  │  │  ├─ math_utils.hpp
│  │  │  └─ string_utils.hpp
│  │  ├─ README.md
│  │  ├─ src
│  │  │  ├─ math_utils.cpp
│  │  │  └─ string_utils.cpp
│  │  └─ tests
│  │     └─ test_main.cpp
│  ├─ py_pkg
│  │  ├─ math_utils.py
│  │  ├─ module.py
│  │  ├─ string_utils.py
│  │  └─ __init__.py
│  └─ README.md
└─ tests
   └─ README.md

```