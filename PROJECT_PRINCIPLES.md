# Engineering Principles

The fundamental engineering principles that guide every technical decision in the AI Video Factory.
When principles conflict, favor the one that protects long-term quality and control.

## 1. Simplicity over Complexity

Prefer the simplest solution that works. Avoid unnecessary abstraction, premature optimization, and hidden magic. Complexity must earn its place.

## 2. Modular Architecture

Build independent, replaceable components with clear boundaries and interfaces. Any module can be upgraded or swapped without breaking the rest.

## 3. Open-Source First

Prefer open, self-hostable tools over proprietary services. Choose closed solutions only when no viable open alternative exists, and document why.

## 4. Self-Hosted First

The system runs on our own infrastructure, under our control. Avoid hard dependencies on third-party managed services for core operations.

## 5. Documentation Before Implementation

Document the intent, design, and key decisions before writing code. Code without a documented rationale is incomplete.

## 6. Security by Design

Treat security as a default, not an afterthought. Manage secrets safely, apply least privilege, and validate all inputs and external data.

## 7. Scalability

Design so the system can grow in volume and capability without a rewrite. Increased output should not demand a proportional increase in effort.

## 8. Maintainability

Write clear, consistent, readable code that others can understand and change. Reduce technical debt continuously rather than letting it accumulate.

## 9. Testability

Build components that can be tested in isolation. Verify behavior with tests before trusting it in production.

## 10. Automation by Default

Automate repetitive tasks — builds, deployments, and production steps. Manual work should be the exception, not the rule.

## 11. Human Oversight for Critical Actions

Keep a human in the loop for high-impact or irreversible actions. Autonomy is the goal, but critical decisions require explicit approval.
