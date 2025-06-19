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
import SafetyCosmeticsCream from '@/views/safety-cosmetics-cream.vue'
import Experts from '@/views/experts.vue'
import Expert from '@/views/expert1.vue'
import Chats from '@/views/chats.vue'
import Analysis from '@/views/analysis.vue'
import AnalysisText from '@/views/analysis-text.vue'
import AnalysisScan from '@/views/analysis-scan.vue'
import AnalysisResult from '@/views/analysis-result.vue'
import AnalysisCompare from '@/views/analysis-compare.vue'
import Reviews from '@/views/reviews.vue'
import Expert1 from '@/views/expert1.vue'
import Expert2 from '@/views/expert2.vue'
import Expert3 from '@/views/expert3.vue'
import Expert4 from '@/views/expert4.vue'
import Expert5 from '@/views/expert5.vue'
import UserInfo from '@/views/user-info.vue'
import Meet from '@/views/meet.vue'
import SafetyCosmeticsBlush from '@/views/safety-cosmetics-blush.vue'
import SafetyCosmeticsBronzer from '@/views/safety-cosmetics-bronzer.vue'
import SafetyCosmeticsEyeliners from '@/views/safety-cosmetics-eyeliners.vue'
import SafetyCosmeticsFoundationCream from '@/views/safety-cosmetics-foundation-cream.vue'
import SafetyCosmeticsGlitters from '@/views/safety-cosmetics-glitters.vue'
import SafetyCosmeticsHighlighter from '@/views/safety-cosmetics-highlighter.vue'
import SafetyCosmeticsLipstick from '@/views/safety-cosmetics-lipstick.vue'
import SafetyCosmeticsPowder from '@/views/safety-cosmetics-powder.vue'
import SafetyCosmeticsShampoo from '@/views/safety-cosmetics-shampoo.vue'


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
      name: 'registration',
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
      path: '/safety-cosmetics-cream',
      name: 'safety-cosmetics-cream',
      component: SafetyCosmeticsCream
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
    },
    {
      path: '/expert1',
      name: 'expert1',
      component: Expert1
    },
    {
      path: '/expert2',
      name: 'expert2',
      component: Expert2
    },
    {
      path: '/expert3',
      name: 'expert3',
      component: Expert3
    },
    {
      path: '/expert4',
      name: 'expert4',
      component: Expert4
    },
    {
      path: '/expert5',
      name: 'expert5',
      component: Expert5
    },
    {
      path: '/user-info',
      name: 'userInfo',
      component: UserInfo,
    },
    {
      path: '/meet',
      name: 'meet',
      component: Meet,
    },
    {
      path: '/safety-cosmetics-blush',
      name: 'safety-cosmetics-blush',
      component: SafetyCosmeticsBlush,
    },
    {
      path: '/safety-cosmetics-bronzer',
      name: 'safety-cosmetics-bronzer',
      component: SafetyCosmeticsBronzer,
    },
    {
      path: '/safety-cosmetics-eyeliners',
      name: 'safety-cosmetics-eyeliners',
      component: SafetyCosmeticsEyeliners,
    },
    {
      path: '/safety-cosmetics-foundation-cream',
      name: 'safety-cosmetics-foundation-cream',
      component: SafetyCosmeticsFoundationCream,
    },
    {
      path: '/safety-cosmetics-glitters',
      name: 'safety-cosmetics-glitters',
      component: SafetyCosmeticsGlitters,
    },
    {
      path: '/safety-cosmetics-highlighter',
      name: 'safety-cosmetics-highlighter',
      component: SafetyCosmeticsHighlighter,
    },
    {
      path: '/safety-cosmetics-lipstick',
      name: 'safety-cosmetics-lipstick',
      component: SafetyCosmeticsLipstick,
    },
    {
      path: '/safety-cosmetics-powder',
      name: 'safety-cosmetics-powder',
      component: SafetyCosmeticsPowder,
    },
    {
      path: '/safety-cosmetics-shampoo',
      name: 'safety-cosmetics-shampoo',
      component: SafetyCosmeticsShampoo,
    }
  ],
})

export default router
