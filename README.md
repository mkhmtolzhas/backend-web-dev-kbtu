## API Endpoints

### User Endpoints
- **POST /api/register/**  
    Registers a new user.  
    **Request body:**
    ```
    {
        "username": string,
        "password": string
    }
    ```

### Authentication Endpoints
- **POST /api/token/**  
    Authenticates a user and returns a token.  
    **Request body:**
    ```
    {
        "username": string,
        "password": string
    }
    ```

- **POST /api/token/refresh/**  
    Refreshes an existing token.  
    **Request body:**
    ```
    {
        "refresh": string
    }
    ```

- **POST /api/token/verify/**  
    Verifies the validity of a token.  

### Chat Endpoints
- **GET /api/chat/**  
    Retrieves a list of all chats.

- **POST /api/chat/**  
    Creates a new chat.  
    **Request body:**
    ```
    {
        "title": string,
        "user": int,
    }
    ```

- **GET /api/chat/{id}**  
    Retrieves a chat.  

- **PUT /api/chat/{id}**  
    Updates a chat.
    **Request body:**
    ```
    {
        "title": string,
        "user": int,
    }
    ```

- **DELETE /api/chat/{id}**  
    Deletes a chat.  

### Message Endpoints
- **GET /api/message/**  
    Retrieves a list of all messages.

- **POST /api/message/**  
    Creates a new message.  
    **Request body:**
    ```
    {
        "content": string,
        "chat": int,
        "user": int,
        "file": null (id, can be null)
    },
    ```

- **GET /api/message/{id}**  
    Retrieves a message.  

- **PUT /api/message/{id}**  
    Updates a message.  
    **Request body:**
    ```
    {
        "content": string,
        "chat": int,
        "user": int,
        "file": null (id, can be null)
    },
    ```

- **DELETE /api/message/{id}**  
    Deletes a message.  

### File Endpoints
- **GET /api/file/**  
    Retrieves a list of all files.

- **POST /api/file/**  
    Uploads a new file.  
    In form-data

- **GET /api/file/{id}**  
    Retrieves a file.  

- **PUT /api/file/{id}**  
    Updates a file.  
    **Request body:**
    ```
    {
        "name": string,
        "content_type": "image/png",
        "url": string
    },
    ```


- **DELETE /api/file/{id}**  
    Deletes a file. 

### LLM Endpoints
- **POST /api/llm/**  
    Interacts with the LLM service.  
    LLM has has "file_url" optional field
    **Request body:**
    ```
    {
        "prompt": string,
        "file_url": string
    }
    ```
