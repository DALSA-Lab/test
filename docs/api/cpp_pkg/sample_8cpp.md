<a id="sample_8cpp"></a>
# File sample.cpp

![][C++]

**Location**: `src/cpppkg/src/sample.cpp`





## Namespaces

* [cpppkg](namespacecpppkg.md#namespacecpppkg)

## Includes

* [sample.h](sample_8h.md#sample_8h)


```mermaid
graph LR
2["sample.h"]
click 2 "sample_8h_source.md#sample_8h_source"

1["src/cpppkg/src/sample.cpp"]
click 1 "sample_8cpp.md#sample_8cpp"
1 --> 2

```


## Source


```cpp
#include "sample.h"

namespace cpppkg {

int Calculator::add(int a, int b) {
    return a + b;
}

int Calculator::multiply(int a, int b) {
    return a * b;
}

}
```


[C++]: https://img.shields.io/badge/language-C%2B%2B-blue (C++)