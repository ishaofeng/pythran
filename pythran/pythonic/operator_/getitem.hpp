#ifndef PYTHONIC_OPERATOR_GETITEM_HPP
#define PYTHONIC_OPERATOR_GETITEM_HPP

#include "pythonic/utils/proxy.hpp"

namespace pythonic {

    namespace operator_ {
        template <class A, class B>
            auto getitem(A const& a, B const& b) -> decltype(a[b]) {
                return a[b];
            }
        PROXY(pythonic::operator_, getitem);

    }

}

#endif

