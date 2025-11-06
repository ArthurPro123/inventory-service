#!/bin/sh

# Step 1: Login to get access_token and refresh_token
LOGIN_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "SuperSecret123"}')

# Extract tokens from the response
ACCESS_TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r '.access_token')
REFRESH_TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r '.refresh_token')

echo "Access Token: $ACCESS_TOKEN"
echo "Refresh Token: $REFRESH_TOKEN"

# Step 2: Access a protected route with the access_token
echo -e "\nAccessing /inventory/ with access_token..."
curl -X GET http://127.0.0.1:5000/inventory/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"

# Step 3: Refresh the access_token using the refresh_token
echo -e "\nRefreshing access_token..."
REFRESH_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/auth/refresh \
  -H "Authorization: Bearer $REFRESH_TOKEN")

# Extract the new access_token
NEW_ACCESS_TOKEN=$(echo "$REFRESH_RESPONSE" | jq -r '.access_token')

echo "New Access Token: $NEW_ACCESS_TOKEN"

# Step 4: Access the protected route again with the new access_token
echo -e "\nAccessing /inventory/ with new access_token..."
curl -X GET http://127.0.0.1:5000/inventory/ \
  -H "Authorization: Bearer $NEW_ACCESS_TOKEN"
