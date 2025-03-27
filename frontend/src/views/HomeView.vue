<script setup>
import { ref, onMounted } from 'vue'

const items = ref([])

onMounted(async () => {
  const res = await fetch('/api/items')
  items.value = await res.json()
})
</script>

<template>
  <h2>Something empty 2</h2>
  <h1>HERE ARE THE ITEMS FROM DB</h1>
  <ul>
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </ul>
</template>