<template>
  <v-container fluid>
    <h1>Meeting Logs</h1>
    <v-data-table :headers="headers" :items="meetingLogs" class="elevation-1">
      <template #item.actions="{ item }">
        <v-btn icon><v-icon>mdi-eye</v-icon></v-btn>
        <v-btn icon><v-icon>mdi-pencil</v-icon></v-btn>
        <v-btn icon color="primary"><v-icon>mdi-robot</v-icon></v-btn>
      </template>
    </v-data-table>
    <!-- TODO: Add dialog/form for creating/editing meeting logs, AI summary -->
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const headers = [
  { title: 'Date', value: 'meeting_date' },
  { title: 'Manager', value: 'manager_name' },
  { title: 'Notes', value: 'notes' },
  { title: 'Actions', value: 'actions', sortable: false },
]
const meetingLogs = ref([
  { id: 1, meeting_date: '2025-04-01', manager_name: 'Manager Name', notes: 'Discussed progress.' },
])
</script>
