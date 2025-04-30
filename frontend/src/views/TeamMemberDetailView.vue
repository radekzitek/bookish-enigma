<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>Profile</v-card-title>
          <v-card-text>
            <!-- TODO: Display team member profile info -->
            <div><strong>Name:</strong> {{ member.first_name }} {{ member.last_name }}</div>
            <div><strong>Position:</strong> {{ member.position }}</div>
            <div><strong>Email:</strong> {{ member.email }}</div>
            <div><strong>Status:</strong> <v-chip :color="member.is_active ? 'green' : 'red'" dark>{{ member.is_active ? 'Active' : 'Inactive' }}</v-chip></div>
            <div><strong>Start Date:</strong> {{ member.start_date }}</div>
            <div><strong>Manager:</strong> {{ member.superior_name }}</div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="8">
        <v-tabs>
          <v-tab>Objectives</v-tab>
          <v-tab>Meetings</v-tab>
          <v-tab>Action Items</v-tab>
          <v-tab>Notes</v-tab>
          <v-tab-item>
            <!-- TODO: List objectives -->
            <div>Objectives go here</div>
          </v-tab-item>
          <v-tab-item>
            <!-- TODO: List meeting logs -->
            <div>Meeting logs go here</div>
          </v-tab-item>
          <v-tab-item>
            <!-- TODO: List action items -->
            <div>Action items go here</div>
          </v-tab-item>
          <v-tab-item>
            <!-- TODO: Show notes -->
            <div>Notes go here</div>
          </v-tab-item>
        </v-tabs>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const member = ref({
  id: 1,
  first_name: 'Alice',
  last_name: 'Smith',
  position: 'Developer',
  email: 'alice@example.com',
  is_active: true,
  start_date: '2024-01-01',
  superior_name: 'Manager Name',
})
</script>
