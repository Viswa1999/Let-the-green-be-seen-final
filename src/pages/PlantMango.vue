<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-teal text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <!-- <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar> -->
          PLANT THE TREE, LET THE NATURE BE GREEN
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs align="right">
          <a href="http://127.0.0.1:8001/">DONATE</a>
        <q-route-tab to="/plant_trees" label="PLANT TREES" />
        
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
    
    <div class="q-pa-md">
    <div class="q-col-gutter-md row items-start">
        <div class="col-4"></div>
      <div class="col-4">
        <q-img src="../assets/mangosampling.jpg" :ratio="4/3">
          <div class="absolute-bottom text-subtitle1 text-center" style="color:yellow">
            The sampling of the Neem tree which you get
          </div>
        </q-img>
      </div>
    </div>
</div>
<center><q-btn color="teal" style="width:20%;padding:10px"><a href="http://127.0.0.1:8002/paydetail/4/">BUY THE TREE NOW</a></q-btn></center>
<center>
<div class="q-pa-md" style="max-width: 600px">
    <q-card>
      <q-tabs
        v-model="tab"
        dense
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
      >
        
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="mails" class="q-pa-none">

          <q-splitter
            v-model="splitterModel"
            style="height: 250px"
          >
          

            <template v-slot:before>
              <q-tabs
                v-model="innerTab"
                vertical
                class="text-teal"
              >
                <q-tab name="innerMails"  label="Mango Tree" />
                <q-tab name="innerAlarms"  label="Usage" />
                <q-tab name="innerMovies"  label="Benefits" />
              </q-tabs>
            </template>

            <template v-slot:after>
              <q-tab-panels
                v-model="innerTab"
                animated
                transition-prev="slide-down"
                transition-next="slide-up"
              >
                <q-tab-panel name="innerMails">
                  <div class="text-h4 q-mb-md">Mango</div>
                  <q-img src="../assets/mangosampling.jpg" :ratio="4/3">
          <div class="absolute-bottom text-subtitle1 text-center" style="color:yellow">
            The sampling of the Neem tree which you get
          </div>
        </q-img>
                </q-tab-panel>

                <q-tab-panel name="innerAlarms">
                  <div class="text-h4 q-mb-md">HOW TO PLANT</div>
                  <p>If you are interested in growing mango trees</p>
                  <p>There are two ways in planting it</p>
                  <p><strong>One either by seeds</strong></p>
                  <p><strong>Or by sampling</strong></p>
                  <p>Neem Trees grows well in arid and tropics region<br>
                  It’s easy to prepare neem seeds for planting as there’s not much to be done. When the fruit falls from the tree the pulp can be removed by rubbing it against a coarse surface when it is wet.</p>
                </q-tab-panel>

                <q-tab-panel name="innerMovies">
                  <div class="text-h4 q-mb-md">BENEFITS</div>
                  <ul>
                  <li>It is very much effective in the dental plaque</li>
                  <li>The mango leaves are disinfectants</li>
                  It cures <li> Malaria<br></li>
                  <li>Fever<br></li>
                  </ul>
                </q-tab-panel>
              </q-tab-panels>
            </template>

          </q-splitter>
        </q-tab-panel>

        <q-tab-panel name="alarms">
          <div class="text-h6">Alarms</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>

        <q-tab-panel name="movies">
          <div class="text-h6">Movies</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
  </center>
  
  </q-layout>
</template>

<script>
import {ref} from 'vue'
export default {
    setup () {
    return {
      tab: ref('mails'),
      innerTab: ref('innerMails'),
      splitterModel: ref(20)
    }
  }

}
</script>

<style>
a{
    color: white;
    text-decoration: none;
    padding: 1%;
    padding-bottom: 19x;
}
button{
  border-sizing: 5px;
}
</style>