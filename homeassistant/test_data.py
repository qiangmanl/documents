#   virtual_storage: 

 
#indifferent 无所谓
hitch_states = [{
    "type": "process",
    "states": """
        reporting = 1,
        receiving = 2,
        resolved = 3,
        disputing = 4,
        rejected = 10
    """
    },
    {
    "type": "weight",
    "states": """
        urgent = 100,
        important = 80,
        standard = 60,
        unimportant = 40,
        noidea = 20,
        indifferent = 0
    """
}]

#suspend  暂停使用
plane_states = \
    [{
        "type" : "rest",
        "states" : """
            healthy = 1,
            unhealthy = 2,
            repairing = 3,
            created = 90,
            suspend = 91,
            dead = 92,
            dirty = 20,
            booking = 11,
            lodging = 12
        """ 
    },
    {
        "type": "public",
        "states": """
            healthy = 1,
            unhealthy = 2,
            repairing = 3,
            created = 90,
            suspend = 91,
            dead = 92,
            dirty = 20
        """
    },
    {
        "type": "park",
        "states": """
            healthy = 1,
            unhealthy = 2,
            repairing = 3,
            created = 90,
            suspend = 91,
            dead = 92,
            dirty = 20
        """
    },

    ]


plane_data = [
    {"area" : "17F",
        "planes" :[{
                "type" : "rest",
                "alias" : "1701"
            },
            {
                "type" : "rest",
                "alias" : "1702"
            },
            {
                "type" : "rest",
                "alias" : "1703"
            },
            {
                "type" : "rest",
                "alias" : "1704"
            },  
            {
                "type" : "rest",
                "alias" : "1705"
        }]
    },
    {"area" : "18F",
        "planes" :[{
                "type" : "rest",
                "alias" : "1801"
            },
            {
                "type" : "rest",
                "alias" : "1802"
            },
            {
                "type" : "rest",
                "alias" : "1803"
            },
            {
                "type" : "rest",
                "alias" : "1804"
            },  
            {
                "type" : "rest",
                "alias" : "1805"
        }]
    }
]


#belong 
#state
entity_data = [
    {
        "structure_type" : "construct",
        "alias" : "1022win",
        "entity_type" :"window",
        "info" : """{
             size : '12*66',
            more_info : 'abc'
        }""",
        "source_info" : """{
             size : '12*66',
            more_info : 'abc'
        }"""
    },
    {
        "structure_type" : "",
        "alias" : "",
        "entity_type" :"",
        "info" : """
        """,
        "source_info" : """
        """
    },
    {
        "structure_type" : "",
        "alias" : "",
        "entity_type" :"",
        "info" : """
        """,
        "source_info" : """
        """
    }
]


