<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class=" bg-teal text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
          </q-avatar>
          Let the green be seen
        </q-toolbar-title>
      </q-toolbar>
       <b><a href="http://127.0.0.1:8002/paydetail/3/" style="float:right;margin-top:12px;">DONATE US</a></b>
      <q-tabs align="right" class="tabs">
        <q-route-tab to="/whytoplanttrees" label="WHY TO PLANT TREES" />
        <q-route-tab to="/plant_trees" label="PLANT TREES" />
        <q-route-tab to="/register" label="REGISTER" />
        <q-route-tab to="/login" label="LOGIN" />
        <q-route-tab to="/new" label="UPLOAD IMAGES" />
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
      
    </q-page-container>
    <div class="q-pa-md">
    <div class="q-col-gutter-md row items-start">
        <div class="col-7">
        <q-img src="../assets/Pichavaram.jpg"
        :ratio="4/3">
          <div class="absolute-full text-subtitle2 flex flex-center">
            <h3>PICHAVARAM</h3>
          </div>
        </q-img>
        </div>

  <div class="col-5">

    <div class="q-pa-md">

    <q-card class="my-card">
      <q-card-section>
        <div class="text-h6">Our Greener Planet</div>
        <div class="text-subtitle2">by Let the Green be seen Team</div>
      </q-card-section>

      <q-tabs v-model="tab" class="text-teal">
        <q-tab label="PLANTING" name="one" />
        <q-tab label="AFFORESTATION" name="two" />
        <q-tab label="OUR WORK" name="three" />
        <q-tab label="PEOPLE" name="four" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="one">
          The process which we done so far is planted as much as trees<br>
          we have planted.<br>
          The amount which we have received is being used for dredging
          <q-img
          src="../assets/plantingtree.jpg"
          :ratio="16/9" />
        </q-tab-panel>

        <q-tab-panel name="two">
          Afforestation is a process where new forests are planted across land without trees. As a forest grows, it naturally removes CO2 from the atmosphere and stores it in its trees
          <q-img
          src="../assets/afforestation.jpg"
          :ratio="16/9" />
        </q-tab-panel>
        <q-tab-panel name="three">
          We have planted trees as much as possible we could.<br>
          The donated amounted amount which user has donated to us<br>
          we have managed it for dredging the ponds and lakes.<br>
          It will be more happier to share the photos to you
          <q-img
          src="../assets/thoor1.jpg"
          :ratio="16/9" />
        </q-tab-panel>
        <q-tab-panel name="four">
          People have bought the trees they want to plant.<br>
          They have even donated to us<br>
          The user have also been posted their images to us and we would be sharing those images<br>
          to all those who are new to our family.<br>
          <strong>This is the small picture planted during the occasion of world plant days.</strong>
          <q-img
          src="../assets/plantingtree.jpg"
          :ratio="16/9" />
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
  </div>
  </div>
    </div>
    <div class="row">
    <div class="col-4">
    <q-img
          src="../assets/quote1.jpg"
          :ratio="4/3" />
    </div>
    <div class="col-1"></div>
    <div class="col">
    <q-img
          src="../assets/quote2.jpg"
          :ratio="1" />
    </div>
    <div class="col-1"></div>
    <div class="col">
    <q-img
          src="../assets/quote3.jpg"
          :ratio="1" />
    </div>
    </div>
    <div class="q-pa-md">
    <q-carousel
      swipeable
      animated
      v-model="slide"
      thumbnails
      infinite
    >
      <q-carousel-slide :name="1" img-src="../assets/forest1.jpg" />
      <q-carousel-slide :name="2" img-src="../assets/beautiful.jpg" />
      <q-carousel-slide :name="3" img-src="../assets/autumn.jpg" />
      <q-carousel-slide :name="4" img-src="../assets/birch_tree.jpg" />
    </q-carousel>
  </div>
  
  
  </q-layout>
</template>

<script>
import axios from 'axios'
import { api } from 'boot/axios'
export default {
  data () {
    return {
      right: false,
      slide: 1,
      tab: 'two',
      }
  },
}
</script>

<style>
.tabs{
  font-size: 10%;
}
a{
  color:white;
  text-decoration:none;
  text-align:right;
}

</style>