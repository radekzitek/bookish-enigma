<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1>Team Members</h1>
        <v-data-table :headers="headers" :items="teamMembers" class="elevation-1">
          <template #item.profile_picture_url="{ item }">
            <v-avatar v-if="item.profile_picture_url" size="32">
              <v-img :src="item.profile_picture_url" />
            </v-avatar>
          </template>
          <template #item.actions="{ item }">
            <v-btn icon :to="`/team/${item.id}`"><v-icon>mdi-eye</v-icon></v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const headers = [
  { title: 'Photo', value: 'profile_picture_url', sortable: false },
  { title: 'First Name', value: 'first_name' },
  { title: 'Last Name', value: 'last_name' },
  { title: 'Position', value: 'position' },
  { title: 'Email', value: 'email' },
  { title: 'Status', value: 'is_active' },
  { title: 'Actions', value: 'actions', sortable: false },
]
const teamMembers = ref([
  // TODO: Fetch from API
  { id: 1, first_name: 'Alice', last_name: 'Smith', position: 'Developer', email: 'alice@example.com', is_active: true, profile_picture_url: '' },
  { id: 2, first_name: 'Bob', last_name: 'Jones', position: 'Designer', email: 'bob@example.com', is_active: true, profile_picture_url: '' },
])
</script>
