#include <boost/mpi.hpp>
#include <iostream>
#include <string>
#include <boost/serialization/string.hpp>
namespace mpi = boost::mpi;

int main()
{
  mpi::environment env;
  mpi::communicator world;

  if (world.rank() == 0) {
    world.send(1, 0, std::string("Hello world!"));
  } else if(world.rank() == 1) {
    std::string msg;
    world.recv(0, 0, msg);
    std::cout << msg << std::endl;
  }

  return 0;
}
