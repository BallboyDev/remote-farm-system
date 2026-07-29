const users = {
    A6042: { auth: 1, }, // 아버지
    B2772: { auth: 1, }, // 어머니
    C0546: { auth: 1, }, // 누나
    D9364: { auth: 1, }, // 매형
    E2282: { auth: 1, }, // 승우
    admin: { auth: 0, }, // 관리자
}

const checkAuth = (id) => {
    const user = users[id];

    if (!user) {
        return { status: 'failure' }
    }
    return { status: 'success', data: { id: id, auth: user.auth } };
}


const login = (id) => {
    const user = users[id];

    if (!user) {
        return { status: 'failure' }
    }
    return { status: 'success', data: { id: id } };
}

module.exports = {
    login,
    checkAuth,
};      