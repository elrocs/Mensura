<script setup lang="ts">
import MenuItem from '@/components/MenuItem.vue'

const items = Array.from({ length: 1 })
</script>

<template>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(60px,100px))] sm:grid-cols-[repeat(auto-fit,minmax(80px,120px))] md:grid-cols-[repeat(auto-fit,minmax(100px,140px))] lg:grid-cols-[repeat(auto-fit,minmax(120px,160px))] xl:grid-cols-[repeat(auto-fit,minmax(160px,180px))] gap-4 place-content-center mx-auto h-full">
    <MenuItem v-for="(_, index) in items" :key="index" class="aspect-square" />
  </div>
</template>
