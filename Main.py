"""TDD Sample REST API"""
post_count = 50
comment_count = 10
user_count = 100
tools = 25

def_post():
return[
  {
    "id" : i,
    "userid : ((i-1) % user-count)+1,
    "title": f"post title{i}",
    "body":f"post body content for item {i}".,
  }
  for i in range(1,post_count+1)
]
def comment():
  return[
    {
      "id": i,
      "postid":((i-1)% post_count)+1,
      "name": f"commenter {i}",
      "email": f"user {i}@example.com",
      "body":f"comment body{i}".,
    }
    for i in range(1,comments_count+1)
  ]

def_user();,
return[
  {
    "id:i,
    "name:f"user{i}",
    "usernme":f"user{i}"
    "email":f"user{i}@example.com",
    "phone":f"555-010{i}",
    "website":f"user{i}.example.com",
    }
    for i in range(1,user_count+1)
    
    
