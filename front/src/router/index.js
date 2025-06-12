import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/main.vue'
import Registration from '@/views/registration.vue'
import CheckNumber from '@/views/check-number.vue'
import MainPage from '@/views/main-page.vue'
import Support from '@/views/support.vue'
import UserAccount from '@/views/user-account.vue'
import WarningAccount from '@/views/warning-account.vue'
import WarningFavourites from '@/views/warning-favourites.vue'
import Favourites from '@/views/favourites.vue'
import SafetyCosmetics from '@/views/safety-cosmetics.vue'
import Experts from '@/views/experts.vue'
import Expert from '@/views/expert.vue'
import Chats from '@/views/chats.vue'
import Analysis from '@/views/analysis.vue'
import AnalysisText from '@/views/analysis-text.vue'
import AnalysisScan from '@/views/analysis-scan.vue'
import AnalysisResult from '@/views/analysis-result.vue'
import AnalysisCompare from '@/views/analysis-compare.vue'
import Reviews from '@/views/reviews.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/main',
      name: 'home',
      component: Main,
    },
    {
      path: '/registration',
      name: 'registartion',
      component: Registration,
    },
    {
      path: '/check-number',
      name: 'number',
      component: CheckNumber,
    },
    {
      path: '/main-page',
      name: 'main',
      component: MainPage,
    },
    {
      path: '/user-account',
      name: 'account',
      component: UserAccount,
    },
    {
      path: '/support',
      name: 'support',
      component: Support
    },
    {
      path: '/warning-account',
      name: 'warningAccount',
      component: WarningAccount,
    },
    {
      path: '/warning-favourites',
      name: "warningFavourites",
      component: WarningFavourites
    },
    {
      path: '/favourites',
      name: 'favourites',
      component: Favourites,
    },
    {
      path: '/safety-cosmetics',
      name: 'safetyCosmetics',
      component: SafetyCosmetics
    },
    {
      path: '/experts',
      name: 'experts',
      component: Experts,
    },
    {
      path: '/expert',
      name: 'expert',
      component: Expert
    },
    {
      path: '/chats',
      name: 'chats',
      component: Chats,
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: Analysis
    },
    {
      path: '/analysis-text',
      name: 'analysisText',
      component: AnalysisText,
    },
    {
      path: '/analysis-scan',
      name: 'analysisScan',
      component: AnalysisScan,
    },
    {
      path: '/analysis-result',
      name: 'analysisResult',
      component: AnalysisResult,
    },
    {
      path: '/analysis-compare',
      name: 'ananlysisCompare',
      component: AnalysisCompare,
    },
    {
      path: '/reviews',
      name : 'reviews',
      component: Reviews,
    }
  ],
})

export default router
