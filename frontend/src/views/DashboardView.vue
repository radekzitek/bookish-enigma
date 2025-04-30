<template>
  <v-container fluid>
    <h1>Dashboard</h1>
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Direct Reports</v-card-title>
          <v-card-text>
            <!-- TODO: List direct reports as cards or chips -->
            <v-chip class="ma-1" v-for="member in directReports" :key="member.id">
              {{ member.first_name }} {{ member.last_name }}
            </v-chip>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Quick Stats</v-card-title>
          <v-card-text>
            <!-- TODO: Show stats like overdue action items, upcoming deadlines -->
            <div>Overdue Action Items: --</div>
            <div>Upcoming KR Deadlines: --</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!-- TODO: Add more dashboard widgets as needed -->
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const directReports = ref([
  { id: 1, first_name: 'Alice', last_name: 'Smith' },
  { id: 2, first_name: 'Bob', last_name: 'Jones' },
])
</script>
