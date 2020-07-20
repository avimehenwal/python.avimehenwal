<template>
  <footer>
    <!-- Add git info created, update(already there), author, commits, contributors -->
    <h6>Footer</h6>
    <ul v-for="(value, k) in $page.git" :key="value.updated">
      <li>
        {{ k }} - {{ value }}
      </li>
    </ul>
  </footer>
</template>