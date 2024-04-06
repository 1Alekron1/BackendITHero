SWAGGER_REGISTER_HR = {
    "tags": ["Boss"],
    "summary": "Register a new HR user",
    "description": "Allows the boss to register a new HR user with provided details.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "New HR user details",
            "schema": {
                "type": "object",
                "properties": {
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                },
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        201: {
            "description": "New HR user registered successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Invalid data provided"}
                },
            },
        },
    },
}


SWAGGER_GET_HRS = {
    "tags": ["Boss"],
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        }
    ],
    "summary": "Get all HR users",
    "description": "Allows the boss to retrieve a list of all registered HR users.",
    "responses": {
        200: {
            "description": "List of HR users retrieved successfully",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "firstName": {"type": "string"},
                        "lastName": {"type": "string"},
                    },
                },
            },
        },
        401: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Unauthorized access"}
                },
            }
        },
    },
}

SWAGGER_CREATE_TASK = {
    "tags": ["Boss"],
    "summary": "Create a new task",
    "description": "Allows the boss to create a new task with provided details.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "New task details",
            "schema": {
                "type": "object",
                "properties": {
                    "hrId": {"type": "integer"},
                    "theme": {"type": "string"},
                    "description": {"type": "string"},
                    "salaryRange": {"type": "string"},
                },
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        201: {
            "description": "Task created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "hrId": {"type": "integer"},
                    "theme": {"type": "string"},
                    "description": {"type": "string"},
                    "salaryRange": {"type": "string"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Invalid data provided"}
                },
            },
        },
    },
}

SWAGGER_SET_TASK_TO_HR = {
    "tags": ["Boss"],
    "summary": "Assign task to an HR user",
    "description": "Allows the boss to assign a task to a specific HR user.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "Task and HR user IDs",
            "schema": {
                "type": "object",
                "properties": {
                    "taskId": {"type": "integer"},
                    "hrId": {"type": "integer"},
                },
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Operation is completed"}
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Invalid data provided"}
                },
            },
        },
    },
}

SWAGGER_SET_TASK_AS_COMPLETED = {
    "tags": ["Boss"],
    "summary": "Mark task as completed",
    "description": "Allows the boss to mark a task as completed.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "Task ID",
            "schema": {"type": "object", "properties": {"taskId": {"type": "integer"}}},
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Operation is completed"}
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Invalid data provided"}
                },
            },
        },
    },
}


SWAGGER_SET_OFFER_TO_RECRUIT = {
    "tags": ["Boss"],
    "summary": "Mark recruit as having received an offer",
    "description": "Allows the boss to mark a recruit as having received an offer.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "Recruit ID",
            "schema": {
                "type": "object",
                "properties": {"recruitId": {"type": "integer"}},
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Operation is completed"}
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Recruit not found"}
                },
            },
        },
    },
}


SWAGGER_UPLOAD_RECRUITS = {
    "tags": ["HR"],
    "summary": "Upload Recruits",
    "description": "Endpoint to upload recruits.",
    "parameters": [
        {
            "name": "taskId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Task ID associated with recruits",
        },
        {
            "name": "files",
            "in": "formData",
            "type": "file",
            "required": True,
            "description": "PDF files containing recruit information",
            "multiple": True,
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "description": "Recruits uploaded successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "taskId": {"type": "integer"},
                    "stepNum": {"type": "integer"},
                    "gotOffer": {"type": "boolean"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Invalid data provided"}
                },
            },
        },
    },
}


SWAGGER_UPDATE_RECRUIT_STEP = {
    "tags": ["HR"],
    "summary": "Update Recruit Step",
    "description": "Endpoint to update recruit step.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "Recruit ID and new step number",
            "schema": {
                "type": "object",
                "properties": {
                    "recruitId": {"type": "integer"},
                    "stepNum": {"type": "integer"},
                },
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {"type": "string", "example": "Operation is completed"}
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such recruit"}},
            },
        },
    },
}

SWAGGER_GET_SELF = {
    "tags": ["Common"],
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        }
    ],
    "summary": "Get Self",
    "description": "Endpoint to get information about the current user.",
    "responses": {
        200: {
            "description": "Information about the current user",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such user"}},
            },
        },
    },
}

SWAGGER_GET_USER = {
    "tags": ["Common"],
    "summary": "Get User",
    "description": "Endpoint to get information about a specific user.",
    "parameters": [
        {
            "name": "userId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "ID of the user to retrieve information about.",
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "description": "Information about the current user",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such user"}},
            },
        },
    },
}

SWAGGER_GET_TASKS_BY_HR = {
    "tags": ["Common"],
    "summary": "Get Tasks by HR",
    "description": "Endpoint to get tasks assigned to a HR user.",
    "parameters": [
        {
            "name": "hrId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "ID of the HR user to fetch tasks for.",
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "description": "List of tasks assigned to the HR user",
            "schema": {
                "type": "array",
                "properties": {
                    "id": {"type": "integer"},
                    "hrId": {"type": "integer"},
                    "theme": {"type": "string"},
                    "description": {"type": "string"},
                    "salaryRange": {"type": "string"},
                    "isCompleted": {"type": "boolean"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such user"}},
            },
        },
    },
}

SWAGGER_GET_RECRUITS_BY_TASK = {
    "tags": ["Common"],
    "summary": "Get Recruits by Task",
    "description": "Endpoint to get recruits associated with a task.",
    "parameters": [
        {
            "name": "taskId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "ID of the task to fetch recruits for.",
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        200: {
            "description": "List of recruits associated with the task",
            "schema": {
                "type": "array",
                "properties": {
                    "id": {"type": "integer"},
                    "taskId": {"type": "integer"},
                    "stepNum": {"type": "integer"},
                    "gotOffer": {"type": "boolean"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such user"}},
            },
        },
    },
}

SWAGGER_ADD_COMMENT_TO_RECRUIT_STEP = {
    "tags": ["Common"],
    "summary": "Add Comment to Recruit Step",
    "description": "Endpoint to add a comment to a recruit's step.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "Recruit ID and new step number",
            "schema": {
                "type": "object",
                "properties": {
                    "recruitId": {"type": "integer"},
                    "text": {"type": "string"},
                    "stepNum": {"type": "integer"},
                },
            },
        },
        {
            "name": "Authorization",
            "in": "header",
            "required": True,
            "description": "Bearer JWT token",
            "type": "string",
        },
    ],
    "responses": {
        201: {
            "description": "Comment added successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "recruitId": {"type": "integer"},
                    "text": {"type": "string"},
                    "stepNum": {"type": "integer"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "No such user"}},
            },
        },
    },
}
SWAGGER_LOGIN = {
    "tags": ["Login"],
    "summary": "User Login",
    "description": "Endpoint for user authentication and login.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "User credentials",
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                },
            },
        }
    ],
    "responses": {
        200: {
            "description": "Login successful",
            "schema": {
                "type": "object",
                "properties": {
                    "JWT": {
                        "type": "string",
                        "example": "JzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikpva",
                    }
                },
            },
        },
        403: {
            "schema": {
                "type": "object",
                "properties": {
                    "msg": {
                        "type": "string",
                        "example": "Incorrect username or password",
                    }
                },
            },
        },
    },
}


GET_COMMENTS_BY_RECRUIT_STEP = {
    "tags": ["Common"],
    "summary": "Get Comments by Recruit Step",
    "description": "Endpoint to get comments by a recruit's step.",
    "parameters": [
        {
            "name": "recruitId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "ID of the recruit to fetch comments for.",
        },
        {
            "name": "stepNum",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Step number to fetch comments for.",
        },
    ],
    "responses": {
        200: {
            "description": "List of comments for the recruit's step",
            "schema": {
                "type": "array",
                "properties": {
                    "id": {"type": "integer"},
                    "recruitId": {"type": "integer"},
                    "text": {"type": "string"},
                    "stepNum": {"type": "integer"},
                },
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "Invalid data"}},
            },
        },
    },
}

GET_RECRUIT_FILE = {
    "tags": ["Common"],
    "summary": "Get Recruit File",
    "description": "Endpoint to get recruit file.",
    "parameters": [
        {
            "name": "recruitId",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "ID of the recruit to fetch file for.",
        }
    ],
    "responses": {
        200: {
            "description": "Recruit file retrieved successfully",
            "schema": {
                "type": "file",
            },
        },
        400: {
            "schema": {
                "type": "object",
                "properties": {"msg": {"type": "string", "example": "Invalid data"}},
            },
        },
    },
}
