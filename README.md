# Krioza Academy — Odoo 20 Training Module

A custom Odoo 20 module developed as part of a hands-on Odoo development course.

The goal is to build a Training Center Management application while learning Odoo's development architecture.

## Project Status

**Initial setup completed:**

- Odoo 20 installed locally on Windows.
- PostgreSQL database configured.
- Custom `krioza_training` module created.
- Module successfully activated in Odoo.
- GitHub repository initialized.

The module is currently a starting point. Course management functionality has not been implemented yet.

## Project Structure

```text
krioza_training/
├── __init__.py
├── __manifest__.py
└── .gitignore
```

- `__manifest__.py` — Defines the module's name, version, dependencies, and installation settings.
- `__init__.py` — Initializes the Python module.
- `.gitignore` — Excludes Python cache and compiled files from Git.

## Local Development

**Requirements:** Odoo 20 and PostgreSQL.

1. Place `krioza_training` inside a custom addons directory.
2. Include the parent directory in Odoo's `addons_path` configuration.
3. Restart Odoo.
4. Open `http://localhost:8069`.
5. Enable Developer Mode.
6. Go to **Apps → Update Apps List**.
7. Find **Krioza Academy** and activate it.

## Planned Development

The project will be expanded throughout the course with Python models, XML views, menus, and training center functionality.

## License

LGPL-3.0, as declared in the module manifest.
