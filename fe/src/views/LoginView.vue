<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Login</h1>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsam quod consequatur libero magni! Illo nulla quae animi explicabo iusto. Rem blanditiis earum, omnis quos sit harum. Veniam accusamus mollitia a?
                </p>
                <p class="font-bold">
                    Don't have an account? <RouterLink :to="{ 'name': 'signup' }" class="underline">Click here</RouterLink> to create one!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign Up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>