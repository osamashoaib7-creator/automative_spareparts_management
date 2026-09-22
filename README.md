# Automotive Spare Parts Management for Odoo 19

[![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)

## Overview
**Automotive Spare Parts Management** (`automotive_spareparts_management`) is a custom Odoo 19 addon that seamlessly extends Odoo's native **Fleet** application. It allows fleet managers to record, assign, and track spare part inventories directly on individual vehicles using Odoo's relational ORM structure.

---

## Key Features

- **Fleet Integration**: Inherits `fleet.vehicle` to integrate a dedicated **Spare Parts** tab into vehicle form views.
- **Relational Auto-Linking**: Establishes a `One2many` / `Many2one` relational link between vehicles and spare parts.
- **Inline Editable Grid**: Add, update, or remove spare parts directly inside the vehicle form view without opening sub-dialogs.
- **Dedicated Spare Parts View**: Access a central list view of all spare parts across the entire fleet via the top navigation menu (`Fleet > Spare Parts`).
- **Cascade On-Delete**: Automatically cleans up associated spare part references when a vehicle record is deleted.

---

## Technical Specifications

| Component | Technical Details |
| :--- | :--- |
| **Odoo Target Version** | `19.0` |
| **Module Dependencies** | `fleet` |
| **Custom Models** | `fleet.spare.part` |
| **Inherited Models** | `fleet.vehicle` |
| **License** | LGPL-3 |

---

## Model Architecture

### `fleet.spare.part` (Custom Model)
- `name` *(Char, Required)*: Name of the spare part.
- `part_number` *(Char, Required)*: Part identification/SKU code.
- `price` *(Float)*: Unit price of the spare part.
- `quantity` *(Integer)*: Quantity assigned (Default: 1).
- `vehicle_id` *(Many2one)*: Relational field referencing `fleet.vehicle`.

### `fleet.vehicle` (Inherited Model)
- `spare_part_ids` *(One2many)*: Relational link mapping to `fleet.spare.part`.

---
