<template>
  <div ref="rendererContainer" @click="onMouseClick" class="renderer-container"></div>
</template>

<script>
import * as THREE from 'three';

export default {
  name: 'Coin234',
  data() {
    return {
      scene: null,
      camera: null,
      renderer: null,
      coin: null,
      coinRotationSpeed: 0,
    };
  },
  mounted() {
    this.initThreeJS();
    this.animate();
  },
  methods: {
    initThreeJS() {
      const width = this.$refs.rendererContainer.clientWidth;
      const height = this.$refs.rendererContainer.clientHeight;

      // Создание сцены
      this.scene = new THREE.Scene();

      // Создание камеры
      this.camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
      this.camera.position.z = 5;

      // Создание рендера
      this.renderer = new THREE.WebGLRenderer();
      this.renderer.setSize(width, height);
      this.$refs.rendererContainer.appendChild(this.renderer.domElement);

      // Создание цилиндра (монеты)
      const geometry = new THREE.CylinderGeometry(1, 1, 0.2, 32);
      const material = new THREE.MeshBasicMaterial({ color: 0xffff00 });
      this.coin = new THREE.Mesh(geometry, material);
      this.scene.add(this.coin);
    },
    onMouseClick(event) {
      const rect = this.$refs.rendererContainer.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      const halfWidth = rect.width / 2;
      const halfHeight = rect.height / 2;

      this.coinRotationSpeed = 0.05 * ((x - halfWidth) / halfWidth);
    },
    animate() {
      requestAnimationFrame(this.animate);

      // Вращение монеты
      if (this.coin) {
        this.coin.rotation.y += this.coinRotationSpeed;
      }

      this.renderer.render(this.scene, this.camera);
    },
  },
};
</script>

<style>
.renderer-container {
  width: 100%;
  height: 100%;
}
</style>
