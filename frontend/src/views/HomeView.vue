<script setup>
import { ref, onMounted } from 'vue'

const items = ref([])

onMounted(async () => {
  const res = await fetch('/api/items')
  items.value = await res.json()
})
</script>

<template>
  <h1>Items</h1>
  <ul>
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </ul>
</template>