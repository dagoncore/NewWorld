# Design Document: Character Equipment System

## Overview

The character equipment system provides an interactive interface for players to equip items on their character within a Ren'Py visual novel. The system uses Ren'Py's screen language and displayable system to create a visual inventory grid and character display with proper image layering. Equipment items modify character stats and persist across game sessions using Ren'Py's save/load system.

The design leverages Ren'Py's built-in capabilities including screen language for UI creation, image composition for layered character display, and variable persistence for state management. All functionality is contained within script.rpy to meet the technical constraints.

## Architecture

The system follows a modular architecture with clear separation between data management, UI presentation, and game integration:

```
┌─────────────────────────────────────────────────────────────┐
│                    Ren'Py Framework                        │
├─────────────────────────────────────────────────────────────┤
│  Equipment System Components                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   Data Layer    │  │  Presentation   │  │ Integration │ │
│  │                 │  │     Layer       │  │    Layer    │ │
│  │ • Equipment     │  │ • Character     │  │ • Save/Load │ │
│  │   State         │  │   Display       │  │ • Screen    │ │
│  │ • Item Data     │  │ • Inventory     │  │   Management│ │
│  │ • Stats         │  │   Grid          │  │ • Actions   │ │
│  │   Calculation   │  │ • UI Screens    │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Key Architectural Decisions:**
- **Single File Constraint**: All code resides in script.rpy as required
- **Screen-Based UI**: Uses Ren'Py's screen language for all user interfaces
- **Image Composition**: Leverages Ren'Py's add statement and layering for character display
- **State Management**: Uses Ren'Py's default variables for automatic save/load integration

## Components and Interfaces

### Data Management Components

**Equipment State Manager**
- Manages currently equipped items for each slot
- Tracks available inventory items
- Calculates total character stats from equipped items
- Interface: Python functions for equip/unequip operations

**Item Definition System**
- Defines equipment items with properties (name, image, stats, slot)
- Provides item lookup and validation
- Interface: Python dictionaries and accessor functions

**Stats Calculator**
- Computes total stats from base values plus equipment modifiers
- Handles stat updates when equipment changes
- Interface: Functions returning calculated stat values

### Presentation Components

**Character Display Screen**
- Renders base character image with equipment layers
- Uses Ren'Py's add statement for proper image layering
- Updates automatically when equipment changes
- Interface: Ren'Py screen with equipment state parameters

**Inventory Grid Screen**
- Displays available items in organized grid layout
- Provides click interactions for equipping items
- Shows item images and basic information
- Interface: Ren'Py screen with inventory data parameters

**Equipment Interface Screen**
- Main screen combining character display and inventory
- Handles user interactions and state updates
- Displays current stats and equipment status
- Interface: Primary Ren'Py screen for the equipment system

### Integration Components

**Screen Actions**
- Custom Ren'Py actions for equip/unequip operations
- Handles screen updates and state synchronization
- Provides feedback for user interactions
- Interface: Ren'Py Action classes

**Save/Load Integration**
- Automatic persistence using Ren'Py's default variables
- Ensures equipment state survives game sessions
- Handles state validation on load
- Interface: Transparent integration with Ren'Py's save system

## Data Models

### Equipment Item Model
```python
# Equipment item structure
equipment_item = {
    "id": "leather_armor",           # Unique identifier
    "name": "Leather Armor",         # Display name
    "image": "items/leather_armor.png",  # Image file path
    "slot": "torso",                 # Equipment slot
    "stats": {                       # Stat modifications
        "strength": 2,
        "agility": 1,
        "intelligence": 0,
        "charisma": 0
    },
    "description": "Basic leather armor"  # Item description
}
```

### Equipment State Model
```python
# Current equipment state
default equipped_items = {
    "underwear": None,    # Currently equipped item ID or None
    "accessory": None,
    "pants": None,
    "torso": None,
    "hat": None,
    "weapon": None
}

# Available inventory items
default inventory_items = {
    "underwear": ["basic_underwear", "silk_underwear"],
    "accessory": ["silver_ring", "gold_necklace"],
    "pants": ["cloth_pants", "leather_pants"],
    "torso": ["cloth_shirt", "leather_armor"],
    "hat": ["cloth_cap", "iron_helmet"],
    "weapon": ["wooden_sword", "iron_sword"]
}
```

### Character Stats Model
```python
# Base character stats
default base_stats = {
    "strength": 10,
    "agility": 10,
    "intelligence": 10,
    "charisma": 10
}

# Calculated total stats (base + equipment)
# Computed dynamically, not stored
```

### Image Asset Organization
```
game/images/
├── character/
│   └── base_character.png          # 640x960 base character
├── equipment/
│   ├── underwear/
│   │   ├── basic_underwear.png
│   │   └── silk_underwear.png
│   ├── accessory/
│   │   ├── silver_ring.png
│   │   └── gold_necklace.png
│   ├── pants/
│   │   ├── cloth_pants.png
│   │   └── leather_pants.png
│   ├── torso/
│   │   ├── cloth_shirt.png
│   │   └── leather_armor.png
│   ├── hat/
│   │   ├── cloth_cap.png
│   │   └── iron_helmet.png
│   └── weapon/
│       ├── wooden_sword.png
│       └── iron_sword.png
└── ui/
    ├── inventory_slot.png          # Empty slot background
    └── equipment_frame.png         # UI frame elements
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Equipment Layering Order Consistency
*For any* combination of equipped items, the character display should maintain the layering order: underwear, accessory, pants, torso, hat, weapon (bottom to top)
**Validates: Requirements 1.2, 1.3**

### Property 2: Equipment Slot Management
*For any* item equipped to a slot, the system should store that item in the correct slot and replace any previously equipped item in that slot
**Validates: Requirements 2.2, 2.4**

### Property 3: Empty Slot Display Consistency
*For any* equipment slot that is empty, the character display should show only the base character for that layer without interference
**Validates: Requirements 1.4**

### Property 4: Inventory Grid Organization
*For any* set of available items, the inventory grid should display them organized by equipment slot type with proper visual formatting
**Validates: Requirements 3.1, 3.3**

### Property 5: Click-to-Equip Functionality
*For any* item clicked in the inventory grid, the system should equip that item to its appropriate slot and remove it from the inventory display
**Validates: Requirements 4.1, 4.2**

### Property 6: Click-to-Unequip Functionality
*For any* equipped item clicked on the character display, the system should unequip the item and return it to the inventory
**Validates: Requirements 4.3**

### Property 7: Stat Calculation Accuracy
*For any* combination of equipped items, the total character stats should equal base stats plus the sum of all equipped item modifiers
**Validates: Requirements 5.2, 5.3, 5.5**

### Property 8: Save/Load State Persistence
*For any* equipment and inventory configuration, saving then loading the game should restore the exact same equipment state and inventory contents
**Validates: Requirements 6.4, 8.1, 8.2, 8.3**

### Property 9: Image Transparency Preservation
*For any* equipment image with transparent areas, those transparent areas should remain transparent in the final character display composite
**Validates: Requirements 1.5, 7.1**

### Property 10: System Consistency Under Operations
*For any* sequence of valid equipment operations (equip/unequip), the system should maintain consistency with no orphaned items or invalid states
**Validates: Requirements 4.5, 8.5**

### Property 11: Error Handling for Missing Assets
*For any* equipment item referencing a missing or invalid image file, the system should handle the error gracefully without crashing
**Validates: Requirements 7.2, 8.4**

## Error Handling

The equipment system implements comprehensive error handling to ensure robust operation:

**Missing Image Files**
- Equipment items with missing images display a placeholder or default image
- System logs warnings for missing assets but continues operation
- Character display gracefully handles missing equipment layers

**Invalid Equipment Operations**
- Attempts to equip items to wrong slots are rejected with user feedback
- System prevents equipping the same item multiple times
- Invalid unequip operations are handled silently

**Save/Load Corruption**
- Corrupted equipment data falls back to default empty equipment state
- Invalid item IDs in save data are filtered out during load
- System validates equipment state consistency after loading

**Memory and Performance**
- Image loading failures are cached to prevent repeated attempts
- Large equipment inventories are handled efficiently through lazy loading
- System monitors memory usage and provides warnings for excessive image sizes

## Testing Strategy

The equipment system uses a dual testing approach combining unit tests for specific scenarios and property-based tests for comprehensive coverage.

**Unit Testing Focus:**
- Specific equipment combinations and edge cases
- UI interaction scenarios with known inputs
- Save/load operations with predefined data sets
- Error conditions with missing or invalid assets
- Integration points between system components

**Property-Based Testing Configuration:**
- Uses Ren'Py's testing framework with custom property test harness
- Each property test runs minimum 100 iterations with randomized inputs
- Tests generate random equipment combinations, item sets, and user interactions
- Property tests validate universal correctness across all possible inputs

**Test Implementation Requirements:**
- Each correctness property implemented as a single property-based test
- Unit tests complement property tests by covering specific examples
- All tests tagged with format: **Feature: character-equipment-system, Property N: [property_text]**
- Tests integrated with Ren'Py's development and CI pipeline

**Coverage Strategy:**
- Property tests ensure universal behavior correctness
- Unit tests catch concrete bugs and integration issues
- Combined approach provides comprehensive validation of system behavior
- Tests validate both functional requirements and non-functional aspects like performance