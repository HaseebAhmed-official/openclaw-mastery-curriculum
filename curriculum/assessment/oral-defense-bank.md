# Oral Defense Bank

## General defense questions

1. What authority did your design create, and why is that authority justified?
2. Which risk in your design is still unresolved, and why did you accept it?
3. What would break first if your chosen provider degraded in quality or rate limits?
4. What part of the official trust model matters most to your artifact?
5. If this had to be used by a trusted team instead of one operator, what would you change?

## Operator track prompts

1. Why is your channel policy safe enough for the users you chose?
2. Which diagnostic commands would you run first if the assistant stopped responding?
3. What makes your workflow operationally maintainable instead of just functional?
4. Where could prompt injection enter your operator workflow?
5. What behavior would force you to stop using your chosen channel setup?

## Production / DevOps prompts

1. Why did you choose this ingress method over the alternatives?
2. Where does identity actually enter the system in your design?
3. What is your rollback strategy if an update changes provider or security behavior?
4. How would you audit detached work in your deployment?
5. What failure mode would your runbook catch fastest?

## Security / Hardening prompts

1. Which finding in your review would you force-fix before production?
2. Which control in your design protects against external-content abuse?
3. What risk remains even with sandboxing?
4. Why is this not a hostile multi-tenant deployment?
5. What would you ask before approving hooks or plugins in this environment?

## Plugin Developer prompts

1. What assumptions does your extension make about compatibility and updates?
2. How would a user misconfigure your design, and what protects them?
3. Which skill or plugin precedence issue is most likely in your artifact?
4. What makes your schema helpful rather than decorative?
5. How would you review the install/update path from a supply-chain perspective?

## Contributor / Core prompts

1. What subsystem boundaries did you intentionally avoid crossing?
2. Which validation gate would you run first and why?
3. How would you discover scoped contributor guidance for your target change?
4. What documentation would have to change if your contribution landed?
5. What is the smallest correct version of your proposal?

## Local Models prompts

1. Why is a local or hybrid model actually justified here?
2. What quality floor would cause you to reject the local path?
3. How did you account for latency, cost, and safety together?
4. What is your fallback if the local model underperforms?
5. Which workload in your design most needs the strongest model available?
