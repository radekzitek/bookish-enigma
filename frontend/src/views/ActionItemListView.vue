<template>
  <v-container fluid>
    <h1>Action Items</h1>
    <v-data-table :headers="headers" :items="actionItems" class="elevation-1">
      <template #item.status="{ item }">
        <v-chip :color="statusColor(item.status)" dark>{{ item.status }}</v-chip>
      </template>
      <template #item.priority="{ item }">
        <v-chip :color="priorityColor(item.priority)" dark>{{ item.priority }}</v-chip>
      </template>
      <template #item.actions="{ item }">
        <v-btn icon><v-icon>mdi-eye</v-icon></v-btn>
        <v-btn icon><v-icon>mdi-pencil</v-icon></v-btn>
      </template>
    </v-data-table>
    <!-- TODO: Add dialog/form for creating/editing action items -->
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const headers = [
  { title: 'Description', value: 'description' },
  { title: 'Assignee', value: 'assigned_to' },
  { title: 'Due Date', value: 'due_date' },
  { title: 'Status', value: 'status' },
  { title: 'Priority', value: 'priority' },
  { title: 'Actions', value: 'actions', sortable: false },
]
const actionItems = ref([
  { id: 1, description: 'Prepare Q2 report', assigned_to: 'Alice', due_date: '2025-05-01', status: 'To Do', priority: 'High' },
])
function statusColor(status: string) {
  switch (status) {
    case 'To Do': return 'grey'
    case 'In Progress': return 'blue'
    case 'Done': return 'green'
    case 'Blocked': return 'red'
    default: return 'grey'
  }
}
function priorityColor(priority: string) {
  switch (priority) {
    case 'High': return 'red'
    case 'Medium': return 'orange'
    case 'Low': return 'green'
    default: return 'grey'
  }
}
</script>
