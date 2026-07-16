const open = () => {
    return { status: 0, data: { message: "Gate opened" } };
}
const close = () => {
    return { status: 0, data: { message: "Gate closed" } };
}

module.exports = {
    openGate: open,
    closeGate: close,
};  