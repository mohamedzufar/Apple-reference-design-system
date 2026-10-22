# Apple Reference Design System

A reusable Apple-inspired design system and Claude Code plugin.

## Add this repository as a Claude Code marketplace

In Claude Code, run:

```text
/plugin marketplace add mohamedzufar/Apple-reference-design-system
/plugin install apple-design-system@mohamedzufar-design-tools
/reload-plugins
```

Then invoke the namespaced skill:

```text
/apple-design-system:apple-design-system
```

You can also inspect the skill at `plugins/apple-design-system/skills/apple-design-system/SKILL.md`.

## Local validation

```bash
claude plugin validate .
claude plugin validate ./plugins/apple-design-system
```

The repository remains a design-system reference site; the plugin package is under `plugins/apple-design-system`.
