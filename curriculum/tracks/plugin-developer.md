# Tools / Protocols Track

## Role

Build reliable, least-authority capabilities and interoperability surfaces that agents and independent clients can use correctly.

## Outcomes

- design discoverable typed tools with unambiguous schemas and errors
- implement timeout, cancellation, idempotency, streaming, and lifecycle behavior
- integrate MCP and A2A while preserving local policy and identity boundaries
- test protocol versions, compatibility, failure, and malicious content
- package dependencies and releases with provenance and rollback
- measure whether interface design improves agent success and repair

## Required Evidence

- LAB-B3, LAB-C4, LAB-C5, LAB-C6, LAB-D3
- tested tool/plugin/protocol implementation
- independent client interoperability
- threat and supply-chain review
- compatibility/version matrix
- delayed changed-client or changed-protocol task

## Advanced Topics

JSON Schema, RPC and streaming, authentication/authorization, capability negotiation, SDK generation, protocol fuzzing, observability conventions, and marketplace governance.

## Capstone Emphasis

Build one narrow capability deeply. Happy-path discovery, ambiguous schemas, or remote capability treated as authorization do not pass.
