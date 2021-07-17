<template>
  <div class="q-pa-md row items-start q-gutter-md">

    <div class="row">
    <div class="col-1"></div>
    <div class="col">
    <q-card
      class="my-card text-white"
      style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
    >
      <q-card-section>
        <div class="text-h6">Trees clean the AIR</div>
        <div class="text-subtitle2">Purification of air</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        {{ lorem }}
      </q-card-section>
    </q-card>
    </div>
    <div class="col-1"></div>
    </div>
  </div>
  <div class="q-pa-md row items-start q-gutter-md">
    <div class="row">
    <div class="col-1"></div>
    <div class="col">
    <q-card
      class="my-card text-white"
      style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
    >
      <q-card-section>
        <div class="text-h6">Trees are natural proetctor</div>
        <div class="text-subtitle2">Trees are eyes-smoothing</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        {{ lorem1 }}
      </q-card-section>
    </q-card>
    </div>
    <div class="col-1"></div>
    </div>
  </div>
  <div class="q-pa-md row items-start q-gutter-md">
    <div class="row">
    <div class="col-1"></div>
    <div class="col">
    <q-card
      class="my-card text-white"
      style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
    >
      <q-card-section>
        <div class="text-h6">Trees are "Friends of farmer"</div>
        <div class="text-subtitle2">It makes the soil fertile</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        {{ lorem2 }}
      </q-card-section>
    </q-card>
    </div>
    <div class="col-1"></div>
    </div>
  </div>
  <div class="q-pa-md row items-start q-gutter-md">
    <div class="row">
    <div class="col-1"></div>
    <div class="col">
    <q-card
      class="my-card text-white"
      style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
    >
      <q-card-section>
        <div class="text-h6">Trees are the home of Birds and animails</div>
        <div class="text-subtitle2">Sweet Home</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        {{ lorem3 }}
      </q-card-section>
    </q-card>
    </div>
    <div class="col-1"></div>
    </div>
  </div>


</template>

<script>
export default {
  setup () {
    return {
      lorem: 'Trees improve air quality by absorbing toxic chemicals from the atmosphere. Pollutant gases and odors such as ammonia, ozone, nitrogen oxides and sulfur dioxide are all absorbed by the leaves of trees. Trees also filter particulates from the air, thus making it clean and free of toxic materials.',
      lorem1: 'Trees mask things. Trees can block parking lots, unsightly views or concrete walls. They also act as sound absorbers from close by highways and streets, and create an excellent aesthetic and eye-soothing green canopy. Wind and dust are also absorbed by trees and they equally reduce glare.',
      lorem2: 'Trees influence land fertility. Without trees, fertile lands can become infertile or even deserts in the long-term. In other words, trees help to keep the soil particles together and prevent soil erosion as well as flooding. Over time, it boots the quality of the soil which not only maintains soil fertility but also replenishes it by anchoring the soil in place. The loss of arable land and the decline in soil fertility is because of topsoil erosion which can be addressed if trees are planted today.',
      lorem3:'Trees protect biodiversity. About 80% of all species of plants and animals survival depend on Trees. An increasing number of animal and plant species are disappearing from the face of the earth, and quite a number are at the verge of extinction. The oak and sycamore, for example, provide an excellent urban habitat for squirrels, bees, birds, and possums. In order to protect the planet’s biodiversity, we need to plant a tree today.'
    }
  }
}
</script>

<style>

</style>