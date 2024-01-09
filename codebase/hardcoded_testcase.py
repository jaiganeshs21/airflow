test_case_1 = {
  "nodes": [
    {
      "id": "1",
      "data": {
        "label": "Taco",
        "componentType": "datasheet_data",
        "component": "WHEN",
        "componentParams": {},
        "entities": ["datasheet"]
      },
      "position": { "x": 0, "y": 0 },
      "type": "workflow"
    },
    {
      "id": "2",
      "data": {
        "label": "Taco 2",
        "component": "IF",
        "componentType": None,
        "componentParams": { "infix_exp": "a==50" },
        "entities": []
      },
      "position": { "x": 200, "y": 150 },
      "type": "workflow"
    },
    {
      "id": "3",
      "data": {
        "label": "Taco 3",
        "component": "IF",
        "componentType": None,
        "componentParams": { "infix_exp": "b==40" },
        "entities": [],
        "if_type": "IF_THEN"
      },
      "position": { "x": 200, "y": 150 },
      "type": "workflow"
    },
    {
      "id": "4",
      "data": {
        "label": "Taco 4",
        "component": "IF",
        "componentType": None,
        "componentParams": { "infix_exp": "b==30" },
        "entities": [],
        "if_type": "ELSE_THEN"
      },
      "position": { "x": 200, "y": 150 },
      "type": "workflow"
    },
    {
      "id": "5",
      "data": {
        "label": "Taco 5",
        "component": "IF",
        "componentType": None,
        "componentParams": { "infix_exp": "c==30" },
        "entities": [],
        "if_type": "ELSE_THEN"
      },
      "position": { "x": 200, "y": 150 },
      "type": "workflow"
    },
    {
      "id": "6",
      "data": {
        "label": "Taco 5",
        "component": "THEN",
        "componentType": "PrintAction",
        "componentParams": {
          "msg": "a==50 & b==40"
        },
        "entities": ["datasheet"],
        "if_type": "IF_THEN"
      },
      "position": { "x": 70, "y": 600 },
      "type": "workflow"
    },
    {
      "id": "7",
      "data": {
        "label": "Taco 3",
        "component": "THEN",
        "componentType": "PrintAction",
        "componentParams": {
          "msg": "a==50"
        },
        "entities": ["datasheet"],
        "if_type": "ELSE_THEN"
      },
      "position": { "x": 70, "y": 600 },
      "type": "workflow"
    },
    {
      "id": "8",
      "data": {
        "label": "Taco 3",
        "component": "THEN",
        "componentType": "PrintAction",
        "componentParams": {
          "msg": "b==30"
        },
        "entities": ["datasheet"],
        "if_type": "IF_THEN"
      },
      "position": { "x": 70, "y": 600 },
      "type": "workflow"
    },
    {
      "id": "9",
      "data": {
        "label": "Taco 3",
        "component": "THEN",
        "componentType": "PrintAction",
        "componentParams": {
          "msg": "c==30"
        },
        "entities": ["datasheet"],
        "if_type": "IF_THEN"
      },
      "position": { "x": 70, "y": 600 },
      "type": "workflow"
    },
    {
      "id": "10",
      "data": {
        "label": "Taco 3",
        "component": "THEN",
        "componentType": "PrintAction",
        "componentParams": {
          "msg": "XX"
        },
        "entities": ["datasheet"],
        "if_type": "ELSE_THEN"
      },
      "position": { "x": 70, "y": 600 },
      "type": "workflow"
    }
  ],
  "edges": [
    {
      "id": "1=>2",
      "source": "1",
      "target": "2",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "2=>3",
      "source": "2",
      "target": "3",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "2=>4",
      "source": "2",
      "target": "4",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "3=>6",
      "source": "3",
      "target": "6",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "3=>7",
      "source": "3",
      "target": "7",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "4=>8",
      "source": "4",
      "target": "8",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "4=>5",
      "source": "4",
      "target": "5",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "5=>9",
      "source": "5",
      "target": "9",
      "type": "workflow",
      "parallel": True
    },
    {
      "id": "5=>10",
      "source": "5",
      "target": "10",
      "type": "workflow",
      "parallel": True
    }
  ]
}

def get_test_case():
    return test_case_1