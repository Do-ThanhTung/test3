# Short note: how black-box testing is applied

For each problem, testing is designed from specification only (input/output contract), not from code internals.

Common process:
1. Identify input domain and output expectation.
2. Split input into equivalence classes:
   - valid classes (accepted data)
   - invalid classes (rejected data)
3. Select boundary values around constraints.
4. Build test cases for:
   - normal valid behavior
   - invalid data and exception behavior
5. Verify actual output/exception against expected result.

Applied per problem:
- Rectangle perimeter/area: positive numeric constraints for dimensions.
- Quadratic equation: partition by discriminant (delta > 0, = 0, < 0) and invalid a = 0.
- Days in month: partition by month groups (31/30/February), leap vs non-leap year, month range boundaries.
- Prime check: partition into prime, composite, n < 2, invalid type.
- Alternating sum: partition by n parity and n > 0 constraint.
- GCD: partition by both non-zero, one zero, and both zero invalid case.
- Sum of factorials: partition by n > 0 valid and n <= 0 invalid; also invalid type.
