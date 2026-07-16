<script>
    import { Button, ButtonGroup, Input } from "@sveltestrap/sveltestrap";
    import WrapperModule from "./components/WrapperModule.svelte";
</script>

<WrapperModule title="Aircon">
    <Button color="primary" disabled>ON</Button>

    <ButtonGroup>
        <Button>up</Button>
        <Button color="secondary" outline>24</Button>
        <Button>down</Button>
    </ButtonGroup>
    <div class="d-flex gap-2 justify-content-between">
        <Button color="primary" outline class="w-100">ON</Button>
        <Button color="danger" outline class="w-100">OFF</Button>
    </div>
</WrapperModule>
