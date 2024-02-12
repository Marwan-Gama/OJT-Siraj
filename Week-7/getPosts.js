// Fetch posts from JSONPlaceholder
fetch("https://jsonplaceholder.typicode.com/posts")
  .then((response) => response.json())
  .then((posts) => {
    // Fetch users from JSONPlaceholder
    return fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((users) => {
        // Map user ids to user objects for easy lookup
        const userIdToUser = {};
        users.forEach((user) => {
          userIdToUser[user.id] = user;
        });

        // Fetch comments from JSONPlaceholder
        return fetch("https://jsonplaceholder.typicode.com/comments")
          .then((response) => response.json())
          .then((comments) => {
            // Map post ids to comment counts
            const postIdToCommentCount = {};
            comments.forEach((comment) => {
              if (!postIdToCommentCount[comment.postId]) {
                postIdToCommentCount[comment.postId] = 0;
              }
              postIdToCommentCount[comment.postId]++;
            });

            // Prepare data for printing
            const data = posts.map((post) => {
              const user = userIdToUser[post.userId];
              return {
                UserName: user.name,
                City: user.address.city,
                "Post Title": post.title.slice(0, 10),
                "Comment Count": postIdToCommentCount[post.id] || 0,
              };
            });

            // Print data using console.table
            console.table(data);
          });
      });
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
