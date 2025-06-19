<template>
  <div class="camera-modal">
    <div class="camera-container">
      <video ref="video" autoplay playsinline class="camera-view"></video>
      <div class="camera-controls">
        <button @click="capture" class="capture-button">
          <img src="/images/icon-camera.svg" alt="Снять фото">
        </button>
        <button @click="closeCamera" class="close-button">
          <img src="/images/icon-close.svg" alt="Закрыть камеру">
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['captured', 'close']);
const video = ref(null);
let stream = null;

const startCamera = async () => {
  try {
    stream = await navigator.mediaDevices.getUserMedia({
      video: {
        facingMode: 'environment',
        width: { ideal: 1280 },
        height: { ideal: 720 }
      }
    });
    video.value.srcObject = stream;
  } catch (error) {
    console.error('Camera error:', error);
    emit('close');
    alert('Не удалось получить доступ к камере');
  }
};

const capture = () => {
  const canvas = document.createElement('canvas');
  canvas.width = video.value.videoWidth;
  canvas.height = video.value.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video.value, 0, 0, canvas.width, canvas.height);

  canvas.toBlob((blob) => {
    const file = new File([blob], 'capture.jpg', { type: 'image/jpeg' });
    emit('captured', file);
    closeCamera();
  }, 'image/jpeg', 0.9);
};

const closeCamera = () => {
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }
  emit('close');
};

onMounted(startCamera);
onUnmounted(closeCamera);
</script>

<style scoped>
.camera-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.camera-container {
  width: 100%;
  max-width: 500px;
  position: relative;
}

.camera-view {
  width: 100%;
  height: auto;
  display: block;
}

.camera-controls {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 40px;
}

.capture-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: white;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.close-button {
  position: absolute;
  top: 20px;
  right: 20px;
  background: rgba(0, 0, 0, 0.5);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.close-button img,
.capture-button img {
  width: 24px;
  height: 24px;
}
</style>
