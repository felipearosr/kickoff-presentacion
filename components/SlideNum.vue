<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const props = defineProps({
  num: { type: [String, Number], required: true },
})

const { clicks, clicksTotal } = useNav()

const isLastClick = computed(() => {
  return clicksTotal.value > 0 && clicks.value >= clicksTotal.value
})
</script>

<template>
  <div class="abs-br m-6 flex gap-2">
    <span
      class="text-sm transition-colors duration-300"
      :class="isLastClick ? 'text-rose-500 font-semibold' : 'opacity-50'"
    >
      {{ num }}
    </span>
  </div>
</template>
