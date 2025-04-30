<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" :permanent="!isMobile">
      <v-list>
        <v-list-item v-for="item in navItems" :key="item.title" :to="item.route" link>
          <v-list-item-icon><v-icon>{{ item.icon }}</v-icon></v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>AI Performance Hub</v-toolbar-title>
      <v-spacer />
      <v-btn icon><v-icon>mdi-account-circle</v-icon></v-btn>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useDisplay } from 'vuetify'

const drawer = ref(true)
const { mobile } = useDisplay()
const isMobile = computed(() => mobile.value)

const navItems = [
  { title: 'Dashboard', icon: 'mdi-view-dashboard', route: '/' },
  { title: 'Team', icon: 'mdi-account-group', route: '/team' },
  { title: 'Goals', icon: 'mdi-target', route: '/goals' },
  { title: 'Meetings', icon: 'mdi-calendar-check', route: '/meetings' },
  { title: 'Action Items', icon: 'mdi-checkbox-marked-outline', route: '/actions' },
  { title: 'AI Insights', icon: 'mdi-robot', route: '/ai' },
]
</script>

<style scoped>
</style>
