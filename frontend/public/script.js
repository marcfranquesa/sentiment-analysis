document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("post-btn");
  button.addEventListener("click", handlePostButtonClick);

  const inputText = document.getElementById("input-text");
  inputText.addEventListener("input", function () {
    updateResponseDiv({ LABEL: "" });
  });
});

async function handlePostButtonClick() {
  const inputText = document.getElementById("input-text").value.trim();

  if (inputText === "") {
    return;
  }

  try {
    const responseData = await postData("/inference/", {
      text: inputText,
    });
    updateResponseDiv(responseData);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

async function postData(url, data) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  return await response.json();
}

function updateResponseDiv(data) {
  const responseDiv = document.getElementById("response");
  responseDiv.innerHTML = "<span>" + data["LABEL"] + "</span>";
}
