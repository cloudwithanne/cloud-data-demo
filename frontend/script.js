const apiUrl = "http://<ALB-DNS>:5000"; // replace with your ALB DNS

async function register() {
  const id = document.getElementById("id").value;
  const name = document.getElementById("name").value;
  const res = await fetch(apiUrl + "/register", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({id, name})
  });
  document.getElementById("response").innerText = (await res.json()).message;
}

async function login() {
  const id = document.getElementById("id").value;
  const name = document.getElementById("name").value;
  const res = await fetch(apiUrl + "/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({id, name})
  });
  document.getElementById("response").innerText = (await res.json()).message;
}
