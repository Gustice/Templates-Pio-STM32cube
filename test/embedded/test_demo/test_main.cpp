#include <unity.h>

void setUp(void) {}

void tearDown(void) {}

void test_toPass(void) {
    TEST_ASSERT_TRUE(1);
}

void test_toFail(void) {
    TEST_ASSERT_TRUE(0);
}

int main(void) {
    for (volatile uint32_t i = 0; i < 4*1000000; i++)
    { // wait some time to allow PC to catch up
    }
    
    UNITY_BEGIN(); // IMPORTANT LINE!
    RUN_TEST(test_toPass);
    RUN_TEST(test_toFail);
    UNITY_END(); // stop unit testing
}
