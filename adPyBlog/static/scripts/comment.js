setTimeout(() => {
  const replyBtn = document.querySelectorAll(".reply-btn");
  const replyContainer = document.querySelectorAll(".reply-container");
  const noReplyContainer = document.querySelectorAll(".no-reply-container");

  const noOption = `
<div
      class="flex flex-col w-full justify-center items-center space-y-5 border rounded-md border-gray-400 p-4"
    >
      <p class="text-xl">Log in to post a comment</p>
      <a
        href="/login"
        class="inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 hover:bg-blue-600"
      >
        Log in
      </a>
    </div>
`;

  function getOption(csrf, commentId, blogId) {
    return `<form action="/blog/comment/" method="post">
    <input type="hidden" value="${csrf}" name="csrfmiddlewaretoken" />
  <input type="hidden" value="${blogId}" name="postId" />
  <input type="hidden" value="${commentId}" name="commentId" />
          <div
            class="px-4 py-2 mt-3 mb-4 bg-white border border-gray-200 rounded-lg rounded-t-lg"
          >
            <label for="comment" class="sr-only">Your comment</label>
            <textarea
              id="comment"
              name="comment"
              rows="4"
              class="w-full px-0 text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none"
              placeholder="Write Reply here..."
              required
            ></textarea>
          </div>
          <button
            type="submit"
            class="inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 hover:bg-blue-600"
          >
            Post Reply
          </button>
        </form>`;
  }

  for (let i = 0; i < replyBtn.length; i++) {
    replyBtn[i].addEventListener("click", () => {
      if (replyContainer.length != 0) {
        if (replyContainer[i].innerHTML.length == 0) {
          replyContainer.forEach((e) => {
            e.innerHTML = "";
          });
          const id = replyBtn[i].id.split("n");
          const token = document.getElementsByName("csrfmiddlewaretoken")[0]
            .value;

          replyContainer[i].innerHTML = getOption(token, id[0], id[1]);
        } else {
          replyContainer[i].innerHTML = "";
        }
      } else {
        if (noReplyContainer[i].innerHTML.length == 0) {
          noReplyContainer.forEach((e) => {
            e.innerHTML = "";
          });
          noReplyContainer[i].innerHTML = noOption;
        } else {
          noReplyContainer[i].innerHTML = "";
        }
      }
    });
  }
}, 300);
