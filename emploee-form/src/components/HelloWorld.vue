<template>
  <label v-if="label">{{ label }}</label>
  <input
    v-bind="$attrs">
    <input 
    :value="modelValue">
    <input
    :placeholder="label">
    <input
    @input="$emit('update:modelValue', $event.target.value)"
    class="field"
  >
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: ''
    },
    modelValue: {
      type: [String, Number],
      default: ''
    }
  }
}
</script>
