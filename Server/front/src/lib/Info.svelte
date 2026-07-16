<script>
    import {
        Input,
        InputGroup,
        InputGroupText,
    } from "@sveltestrap/sveltestrap";
    import WrapperModule from "./components/WrapperModule.svelte";
</script>

<WrapperModule title="Info">
    <InputGroup>
        <InputGroupText class="w-25">서버</InputGroupText>
        <Input class="w-25" value="정상" readonly />
        <InputGroupText class="w-25">모듈 연결</InputGroupText>
        <Input class="w-25" value="정상" readonly />
    </InputGroup>

    <InputGroup>
        <InputGroupText class="w-25">날씨</InputGroupText>
        <Input class="w-25" value="맑음" readonly />
        <InputGroupText class="w-25">기온</InputGroupText>
        <Input class="w-25" value="25°C" readonly />
    </InputGroup>
    <InputGroup>
        <InputGroupText class="w-25">방 안 온도</InputGroupText>
        <Input class="w-25" value="22°C" readonly />
        <InputGroupText class="w-25">습도</InputGroupText>
        <Input class="w-25" value="60%" readonly />
    </InputGroup>

    <!-- <div>서버 상태, 모듈 연결 상태</div>
    <div>기온, 습도, 날씨</div>
    <div>방 안 온도, 정보</div> -->
</WrapperModule>
