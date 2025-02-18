<script setup lang="ts">

    import {
        Card,
        CardTitle,
    } from '@/components/ui/card'

    import { Icon } from '@iconify/vue'

    defineProps<{icon: string}>()

</script>

<template>
    <Card class="relative aspect-square flex items-center justify-center p-4 group cursor-pointer">
      
      <Icon :icon="icon" class="w-[50%] h-[50%] text-muted-foreground" />
  
      <CardTitle class="absolute bottom-2 right-2 text-muted-foreground text-sm opacity-0 transition-opacity duration-100 group-hover:opacity-100">
        <slot />
      </CardTitle>
  
    </Card>
  </template>
  