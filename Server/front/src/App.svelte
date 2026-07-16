<script lang="ts">
  import { onMount } from "svelte";

  import Aircon from "./lib/Aircon.svelte";
  import Gate from "./lib/Gate.svelte";
  import Info from "./lib/Info.svelte";
  import Login from "./lib/Login.svelte";
  import Watering from "./lib/Watering.svelte";

  let loginStatus = false;

  onMount(() => {
    // 페이지가 로드될 때 실행되는 코드
    const user = localStorage.getItem("userId");
    if (user) {
      loginStatus = true;
    }
  });
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  />
</svelte:head>

<main id="main">
  <div class="header">
    <div>
      <h2 class="mainTitle">Remote Farm System</h2>
      <p class="subTitle">원격 농장 제어 대시보드</p>
    </div>
    <Login />
  </div>

  <section class="content">
    <!-- 시스템 및 환경 정보 -->
    <Info />

    {#if !!loginStatus}
      <div class="controlGrid">
        <!-- 게이트 컨트롤러 -->
        <Gate />

        <!-- 에어컨 컨트롤러 -->
        <Aircon />

        <!-- 관수 시스템 컨트롤러 -->
        <Watering />
      </div>
    {/if}
  </section>

  <div class="footer d-flex justify-content-between align-items-center">
    <p class="font-size-sm text-muted">ballboyDev@copyleft</p>
    <p class="font-size-sm text-muted">마지막 업데이트: 2026-07-13</p>
  </div>
</main>

<style>
  @import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css";

  #main {
    min-height: 100dvh;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background: #f5f7fa;
  }

  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 0.75rem;
  }

  .mainTitle {
    font-size: 1.5rem;
    font-weight: bold;
    line-height: 1.2;
  }

  .subTitle {
    margin-top: 0.25rem;
    color: #6b7280;
    font-size: 0.875rem;
  }

  .loginInfo {
    flex-shrink: 0;
    color: #374151;
    font-size: 0.875rem;
  }

  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .controlGrid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
  }

  @media (max-width: 520px) {
    #main {
      padding: 0.75rem;
    }

    .header,
    .footer {
      flex-direction: column;
      align-items: flex-start;
    }
  }
</style>
