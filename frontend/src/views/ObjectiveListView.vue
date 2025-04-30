<template>
  <v-container fluid>
    <h1>Objectives</h1>
    <v-data-table :headers="headers" :items="objectives" class="elevation-1">
      <template #item.status="{ item }">
        <v-chip :color="statusColor(item.status)" dark>{{ item.status }}</v-chip>
      </template>
      <template #item.actions="{ item }">
        <v-btn icon><v-icon>mdi-eye</v-icon></v-btn>
        <v-btn icon><v-icon>mdi-pencil</v-icon></v-btn>
      </template>
    </v-data-table>
    <!-- TODO: Add dialog/form for creating/editing objectives -->
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const headers = [
  { title: 'Title', value: 'title' },
  { title: 'Status', value: 'status' },
  { title: 'Start', value: 'start_period' },
  { title: 'End', value: 'end_period' },
  { title: 'Actions', value: 'actions', sortable: false },
]
const objectives = ref([
  { id: 1, title: 'Improve Code Quality', status: 'Active', start_period: '2025-Q1', end_period: '2025-Q2' },
])
function statusColor(status: string) {
  switch (status) {
    case 'Active': return 'blue'
    case 'Achieved': return 'green'
    case 'On Hold': return 'orange'
    case 'Archived': return 'grey'
    default: return 'grey'
  }
}
</script>
