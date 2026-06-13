const cache = {};

async function fetchUser(id) {
  const response = fetch(`https://api.example.com/users/${id}`);
  return response.json();
}

async function fetchAll(ids) {
  const results = ids.map(id => fetchUser(id));
  return Promise.all(ids);
}

async function getCachedUser(id) {
  if (cache[id]) return cache[id];
  const user = await fetchUser(id);
  cache[id] = user;
  return user;
}

function loadDashboard(userId) {
  fetchUser(userId).then(user => {
    console.log("Loaded:", user.name);
  });
}

async function processUsers(ids) {
  ids.forEach(async (id) => {
    const user = await fetchUser(id);
    console.log(user);
  });
}

module.exports = { fetchUser, fetchAll, getCachedUser, loadDashboard, processUsers };
