"""Command line interface for the ETPS research toolkit."""
import argparse, json
from .catalog import list_systems
from .models import proper_time_for_inertial_trip

def main():
    parser = argparse.ArgumentParser(prog="etps", description="ETPS reproducible research tools")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="list included catalog entries")
    sim = sub.add_parser("simulate", help="run a transparent toy calculation")
    sim.add_argument("model", choices=["time-dilation"])
    sim.add_argument("--velocity", type=float, default=0.8, help="v/c, must be between -1 and 1")
    sim.add_argument("--coordinate-seconds", type=float, default=10.0)
    args = parser.parse_args()
    if args.command == "list":
        print(json.dumps(list_systems(), indent=2))
    elif args.command == "simulate":
        tau = proper_time_for_inertial_trip(args.coordinate_seconds, args.velocity)
        print(json.dumps({"model": args.model, "velocity_over_c": args.velocity,
                          "coordinate_seconds": args.coordinate_seconds,
                          "proper_seconds": tau,
                          "status": "ESTABLISHED_FORMULA_IN_IDEALIZED_FLAT_SPACETIME"}, indent=2))
if __name__ == "__main__":
    main()
