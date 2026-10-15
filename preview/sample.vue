<script setup lang="ts">
import { ref } from "vue";
const count = ref(2);
function increment(): void {
  count.value += 1;
}
</script>

<template>
  <!-- Tags, attributes, interpolation and embedded TypeScript -->
  <button class="counter" :disabled="count > 42" @click="increment">
    Deep Blue: {{ count }}
  </button>
</template>

<style scoped>
.counter:hover {
  color: #81cfe0;
  padding: 8px 12px;
}
</style>
