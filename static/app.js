const deviceGrid = document.getElementById("device-grid");
const toast = document.getElementById("toast");

async function fetchDevices() {
  try {
    const response = await fetch("/api/devices");
    if (!response.ok) {
      throw new Error("デバイス一覧の取得に失敗しました。");
    }
    return await response.json();
  } catch (error) {
    showToast(error.message, "error");
    return [];
  }
}

function showToast(message, type = "success") {
  toast.textContent = message;
  toast.className = `toast visible ${type}`;
  clearTimeout(showToast.timeoutId);
  showToast.timeoutId = setTimeout(() => {
    toast.className = "toast hidden";
  }, 3500);
}

async function sendWake(mac) {
  try {
    const response = await fetch("/api/wake", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ mac }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Wake-on-LAN送信中にエラーが発生しました。");
    }

    const result = await response.json();
    showToast(result.message || "送信に成功しました。", "success");
  } catch (error) {
    showToast(error.message, "error");
  }
}

function createDeviceCard(device) {
  const card = document.createElement("button");
  card.className = "device-card";
  card.type = "button";
  card.textContent = device.name;
  card.addEventListener("click", () => sendWake(device.mac));
  return card;
}

async function init() {
  const devices = await fetchDevices();
  if (!devices.length) {
    deviceGrid.innerHTML = "<p>登録されたデバイスがありません。</p>";
    return;
  }

  deviceGrid.innerHTML = "";
  devices.forEach((device) => {
    const card = createDeviceCard(device);
    deviceGrid.appendChild(card);
  });
}

init();
