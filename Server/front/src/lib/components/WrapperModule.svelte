<script lang="ts">
    let { children = null, state = null, title } = $props();
</script>

<div class="moduleCard">
    <div class="d-flex align-items-center mb-2">
        <h3>{title}</h3>

        {#if state === null}
            <!-- <div
                class={`state ${state === 1 ? "bg-success" : "bg-danger"}`}
            ></div> -->
            <div class="d-flex"><p class={`state `}></p></div>
        {/if}
    </div>
    <div class="moduleBody">
        {@render children?.()}
    </div>
</div>

<style>
    .moduleCard {
        padding: 1rem 0.5rem;
        width: 100%;
        /* min-height: 10rem; */
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06);
    }

    h3 {
        margin-bottom: 0.75rem;
        font-size: 1rem;
        line-height: 1.2;
    }

    .state {
        width: 0.5rem;
        height: 0.5rem;
        line-height: 1rem;
        margin-left: 0.5rem;
        border-radius: 50%;
        background: #4ade80;
    }

    .moduleBody {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        color: #374151;
    }
</style>
